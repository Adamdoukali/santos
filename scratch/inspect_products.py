import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('user_store_products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

products = data.get('products', [])
print(f"Total raw products: {len(products)}")
for i, p in enumerate(products, 1):
    title = p.get('title')
    handle = p.get('handle')
    ptype = p.get('product_type')
    tags = p.get('tags')
    variants = p.get('variants', [])
    price = variants[0].get('price') if variants else 'N/A'
    images = p.get('images', [])
    print(f"{i}. [{ptype or 'NoType'}] {title} | Price: {price} | Handle: {handle} | Tags: {tags} | Images: {len(images)}")
