import os
import re
import glob

html_files = glob.glob("*.html")

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def replace_image(match):
        full_tag = match.group(0)
        if 'phone-mockup' in content or 'hero' in content: # rough heuristics but let's just do src replacement
            pass
        return 'src="logo.png"'
        
    new_content = re.sub(r'src="data:image/[^"]+"', 'src="logo.png"', content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Optimized: {filepath}")
    else:
        print(f"No changes needed for: {filepath}")
