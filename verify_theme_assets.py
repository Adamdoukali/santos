import os
import re

theme_dir = 'santos-shopify-theme'
assets_dir = os.path.join(theme_dir, 'assets')
existing_assets = set(os.listdir(assets_dir))

pattern = re.compile(r"['\"]([^'\"]+\.[a-zA-Z0-9_-]+)['\"]\s*\|\s*asset_url")
missing = []
found = []

for root, dirs, files in os.walk(theme_dir):
    for f in files:
        if f.endswith('.liquid') or f.endswith('.json'):
            path = os.path.join(root, f)
            with open(path, encoding='utf-8') as fh:
                content = fh.read()
                matches = pattern.findall(content)
                for m in matches:
                    if m not in existing_assets:
                        missing.append((path, m))
                    else:
                        found.append((path, m))

print(f"Valid asset references: {len(found)}")
print(f"Missing assets: {len(missing)}")
for p, m in missing:
    print(f"  {p} -> {m}")
