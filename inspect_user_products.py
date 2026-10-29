import json
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

with open('user_store_products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

products = data.get('products', [])
print(f"Total products: {len(products)}")

for p in products:
    title = p.get('title')
    handle = p.get('handle')
    ptype = p.get('product_type')
    tags = p.get('tags')
    variants = p.get('variants', [])
    price = variants[0].get('price') if variants else '0'
    img_count = len(p.get('images', []))
    options = [opt['name'] + ': ' + ', '.join(opt['values']) for opt in p.get('options', [])]
    print(f"ID: {p.get('id')} | {title} | ${price} | Type: {ptype} | Imgs: {img_count}")
    print(f"   Options: {options}")
    print(f"   Tags: {tags}")
    print("-" * 50)
