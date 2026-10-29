import json

with open('santos_real_products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for p in products:
    price = p['price']
    p['price_formatted'] = f"{price:.2f} MAD"

with open('santos_real_products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print("Updated santos_real_products.json with MAD currency!")
