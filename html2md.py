from bs4 import BeautifulSoup
import os 

def convert_directory_to_markdown(directory_path, output_directory=None):
    # If output directory is specified and doesn't exist, create it
    if output_directory and not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.htm'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    xhtml_content = f.read()
                markdown_content = xhtml_to_markdown(xhtml_content).replace('\r\n', '\n')
                md_filename = os.path.splitext(file)[0].replace(' ', '_') + ".md"
                
                # Decide where to save the markdown file
                if output_directory:
                    save_path = os.path.join(output_directory, md_filename)
                else:
                    save_path = os.path.join(root, md_filename)
                
                with open(save_path, 'w', encoding='utf-8') as f:
                    f.write(markdown_content)

def global_substitutions(xhtml):
    """Perform global substitutions before processing."""
    xhtml = xhtml.replace('&#160;', ' ')
    return xhtml

def process_elements(tag):
    # Bold for 'Name' class
    if 'Name' in tag.attrs.get('class', []):
        tag.string = f"**{tag.get_text(' ', strip=True)}**"
    # Code backticks for 'Dyalog', 'DyalogExample', and 'h3Right' classes
    elif any(d_class in tag.attrs.get('class', []) for d_class in ['Dyalog', 'DyalogExample', 'h3Right']):
        tag.string = f"`{tag.get_text(' ', strip=True)}`"
    # Italic for 'Italic' class
    elif 'Italic' in tag.attrs.get('class', []):
        tag.string = f"*{tag.get_text(' ', strip=True)}*"
    return tag

def convert_code_blocks(pre_tags):
    """Convert <pre> tags to markdown code blocks."""
    for pre in pre_tags:
        for br in pre.find_all("br"):
            br.replace_with("\n")
        code_content = pre.get_text()
        if 'nonAPLcode' in pre.attrs.get('class', []):
            markdown_code = f"```\n{code_content}\n```\n"
        else:
            markdown_code = f"```apl\n{code_content}\n```\n"
        pre.replace_with(markdown_code)

def xhtml_to_markdown(xhtml):
    """Convert XHTML to markdown."""
    xhtml = global_substitutions(xhtml)
    soup = BeautifulSoup(xhtml, 'lxml-xml')

    # Convert <title> tags to markdown H1 headers
    # for title in soup.find_all('title'):
    #     title.replace_with(f"# {title.get_text().strip()}\n")

    # Remove <title> tags
    for title in soup.find_all('title'):
        title.replace_with('')

    # Convert <h1>, <h2>, ... to markdown headers
    for hx in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        hx.replace_with(f"{'#' * int(hx.name[1])} {hx.get_text().strip()}\n")

    # Process <code> tags
    for code_tag in soup.find_all('code'):
        code_tag.replace_with(f"`{code_tag.get_text(' ', strip=True)}`")

    # Process all elements with the desired classes
    for tag in soup.find_all(True, class_=['Name', 'Dyalog', 'DyalogExample', 'h3Right', 'Italic']):
        process_elements(tag)

    # Cross-references
    for xref in soup.find_all('MadCap:xref'):
        href = xref.attrs.get('href', '')
        target_filename, _, anchor = href.partition('#')
        target_filename = target_filename.replace(' ', '_').replace('.htm', '.md')
        markdown_link = f'[{xref.get_text()}]({target_filename}#{anchor})'
        xref.replace_with(markdown_link)

    # Convert <p> tags to markdown paragraphs
    for p in soup.find_all('p'):
        p.replace_with(f"\n{p.get_text().strip()}\n")

    # Convert <table> to markdown tables
    for table in soup.find_all('table'):
        rows = table.find_all('tr')
        table_data = []
        for row in rows:
            cols = row.find_all(['td', 'th'])
            table_data.append("| " + " | ".join([
                col.get_text(' ', strip=True).replace('\n', ' ')
                for col in cols
            ]) + " |")
        table_data.insert(1, "| --- " * len(rows[0].find_all(['td', 'th'])) + "|")
        table.replace_with("\n".join(table_data) + "\n")

    # Convert <ul> to markdown unordered lists
    for ul in soup.find_all('ul'):
        ul.replace_with("\n".join([
            f"- {li.get_text()}"
            for li in ul.find_all('li')
        ]))

    # Convert <ol> to markdown ordered lists
    for ol in soup.find_all('ol'):
        ol.replace_with("\n".join([
            f"{i+1}. {li.get_text()}"
            for i, li in enumerate(ol.find_all('li'))
        ]))

    # Convert <pre class="APLCode"> and <pre class="nonAPLcode"> 
    # to markdown fenced code blocks
    convert_code_blocks(soup.find_all('pre', class_=['APLCode', 'nonAPLcode']))

    return soup.get_text()

if __name__ == '__main__':
    convert_directory_to_markdown(
        'RIDE', 
        output_directory='/Users/stefan/work/dydoc/docs/'
    )