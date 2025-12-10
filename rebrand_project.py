import os

root_dir = "."
replacements = {
    "TalentSphere": "GiftedForge",
    "talentsphere": "giftedforge",
    "TALENTSPHERE": "GIFTEDFORGE"
}

extensions = ['.html', '.css', '.js', '.md']

count = 0
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if any(filename.endswith(ext) for ext in extensions):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                for old, new in replacements.items():
                    content = content.replace(old, new)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated: {filepath}")
                    count += 1
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

print(f"Total files updated: {count}")
