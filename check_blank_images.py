import json

with open('user_store_products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data.get('products', []):
    title = p.get('title', '')
    if any(k in title.lower() for k in ['trensh', 'black vale', 'fleece']):
        print(f"Product: {title}")
        print(f"  ID: {p.get('id')}")
        print(f"  Image: {p.get('image')}")
        imgs = p.get('images', [])
        print(f"  Images count: {len(imgs)}")
        for img in imgs[:2]:
            print(f"    src: {img.get('src')}")
        print("-" * 50)
