import json
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('user_store_products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data.get('products', []):
    html = p.get('body_html', '')
    if html:
        clean = re.sub(r'<[^>]+>', ' ', html).strip()
        clean = ' '.join(clean.split())
        print(f"=== {p.get('title')} ===")
        print(clean)
