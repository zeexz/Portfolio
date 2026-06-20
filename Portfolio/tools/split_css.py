import os
import re

css_path = r"d:\Projects\Portfolio\css\style.css"
css_dir = r"d:\Projects\Portfolio\css"

with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

# Pattern to find section headers
# e.g., /* ==========================================================================
#          Navigation
#          ========================================================================== */
pattern = r"/\* ==========================================================================\n\s*(.*?)\n\s*========================================================================== \*/\n"

sections = re.split(pattern, css_content)

# sections[0] is everything before the first header (usually empty)
# sections[1] is the first header title
# sections[2] is the content
# ...

module_imports = []

def sanitize_filename(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '-', name)
    return name.strip('-') + ".css"

for i in range(1, len(sections), 2):
    title = sections[i]
    content = sections[i+1]
    
    filename = sanitize_filename(title)
    
    # We'll save these into css/modules/
    modules_dir = os.path.join(css_dir, "modules")
    os.makedirs(modules_dir, exist_ok=True)
    
    module_path = os.path.join(modules_dir, filename)
    with open(module_path, "w", encoding="utf-8") as f:
        # Add the header back for readability in the split files
        f.write(f"/* {title} */\n")
        f.write(content.strip() + "\n")
    
    module_imports.append(f"@import url('modules/{filename}');")
    print(f"Created {filename}")

# Re-write the main style.css with imports
main_css_content = "\n".join(module_imports)
with open(css_path, "w", encoding="utf-8") as f:
    f.write(main_css_content)

print("CSS successfully split and main style.css updated.")
