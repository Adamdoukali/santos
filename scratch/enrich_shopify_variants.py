import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('user_store_products.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

with open('santos_real_products.json', 'r', encoding='utf-8') as f:
    real_products = json.load(f)

raw_by_id = {p['id']: p for p in raw_data.get('products', [])}

for p in real_products:
    pid = p['id']
    raw = raw_by_id.get(pid)
    if raw:
        variants = raw.get('variants', [])
        p['shopify_product_id'] = pid
        p['shopify_handle'] = raw.get('handle')
        p['shopify_url'] = f"https://a9xpr3-x0.myshopify.com/products/{raw.get('handle')}"
        if variants:
            p['variant_id'] = variants[0]['id']
            p['variants_map'] = [
                {
                    'id': v['id'],
                    'title': v.get('title'),
                    'price': float(v.get('price', p['price'])),
                    'available': v.get('available', True)
                }
                for v in variants
            ]
        else:
            p['variant_id'] = pid
            p['variants_map'] = []

with open('santos_real_products.json', 'w', encoding='utf-8') as f:
    json.dump(real_products, f, indent=2, ensure_ascii=False)

print("Updated santos_real_products.json with Shopify variant IDs and URLs!")
