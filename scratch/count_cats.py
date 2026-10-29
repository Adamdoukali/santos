import json

with open('santos_real_products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

cats = {}
for p in products:
    c = p.get('category')
    cats[c] = cats.get(c, 0) + 1

print("Categories count:")
for k, v in cats.items():
    print(f"- {k}: {v} products")
