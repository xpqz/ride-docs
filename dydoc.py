import os
import yaml

def generate_nav(path="."):
    items = []
    for name in sorted(os.listdir(path)):
        full_path = os.path.join(path, name)
        if name.startswith("."):
            continue

        if os.path.isdir(full_path):
            item = {name: generate_nav(full_path)}
        elif full_path.endswith(".md"):
            item = full_path[:] # skip leading './' 
        else:
            continue

        items.append(item)
    
    return items

def write_mkdocs_yml(nav, site_name="My Project", theme="readthedocs"):
    config = {
        "site_name": site_name,
        "nav": nav,
        "theme": theme,
    }
    
    with open("mkdocs.yml", "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)

if __name__ == "__main__":
    nav = generate_nav('docs')
    write_mkdocs_yml(nav)