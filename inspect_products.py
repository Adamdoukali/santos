import json

with open("balmoral_products.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Total products: {len(data['products'])}")
for p in data["products"]:
    variants = p.get("variants", [])
    price = variants[0].get("price", "0") if variants else "0"
    p_type = p.get("product_type", "General")
    title = p.get("title", "")
    print(f"{title} | ${price} CAD | {p_type}")
