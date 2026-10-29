import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('user_store_products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data.get('products', []):
    print(f"Product: {p.get('id')} - {p.get('title')}")
    variants = p.get('variants', [])
    for v in variants:
        print(f"   Variant ID: {v.get('id')} | Title: {v.get('title')} | Price: {v.get('price')} | Available: {v.get('available')}")
