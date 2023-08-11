import os
from bs4 import BeautifulSoup

def convert_directory_to_markdown(directory_path):
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.htm'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    xhtml_content = f.read()
                markdown_content = xhtml_to_markdown(xhtml_content).replace('\r\n', '\n')
                md_filename = os.path.splitext(file)[0].replace(' ', '_') + ".md"
                with open(os.path.join(root, md_filename), 'w', encoding='utf-8') as f:
                    f.write(markdown_content)


def process_elements(tag):
    """Utility function to replace elements with the desired markdown."""
    # Bold for 'Name' class
    if 'Name' in tag.attrs.get('class', []):
        tag.replace_with(f"**{tag.get_text(' ', strip=True)}**")
    # Code backticks for 'Dyalog' class
    elif 'Dyalog' in tag.attrs.get('class', []):
        tag.replace_with(f"`{tag.get_text(' ', strip=True)}`")
    # Code backticks for 'h3Right' class
    elif 'h3Right' in tag.attrs.get('class', []):
        tag.string = f"`{tag.get_text(' ', strip=True)}`"
    return tag

def convert_code_blocks(pre_tags):
    """Convert <pre> tags to markdown code blocks."""
    for pre in pre_tags:
        markdown_code = "```apl\n" + pre.get_text() + "\n```"
        pre.replace_with(markdown_code)

def xhtml_to_markdown(xhtml):
    """Convert XHTML to markdown."""
    soup = BeautifulSoup(xhtml, 'html.parser')

    # Convert <title> tags to markdown H1 headers
    for title in soup.find_all('title'):
        title.replace_with(f"# {title.get_text()}\n")

    # Process all elements with the desired classes
    for tag in soup.find_all(True, class_=['Name', 'Dyalog', 'h3Right']):
        process_elements(tag)

    # Convert <p> tags to markdown paragraphs
    for p in soup.find_all('p'):
        p.replace_with(f"\n{p.get_text()}\n")

    # Convert <h1>, <h2>, ... to markdown headers
    for hx in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        hx.replace_with(f"\n{'#' * int(hx.name[1])} {hx.get_text()}\n")

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

    # Convert <pre class="APLCode"> to markdown fenced code blocks
    convert_code_blocks(soup.find_all('pre', class_='APLCode'))

    return soup.get_text()

if __name__ == '__main__':
    convert_directory_to_markdown('test')