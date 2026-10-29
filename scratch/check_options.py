import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('user_store_products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data.get('products', []):
    desc = p.get('body_html', '')
    variants = p.get('variants', [])
    options = p.get('options', [])
    print(f"--- {p.get('title')} ---")
    print(f"  Options: {[opt.get('name') + ': ' + ', '.join(opt.get('values', [])) for opt in options]}")
    print(f"  Desc: {desc[:150] if desc else 'None'}")
