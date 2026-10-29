import urllib.request
import json

base_url = "https://a9xpr3-x0.myshopify.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

print("Checking products.json...")
try:
    req = urllib.request.Request(f"{base_url}/products.json?limit=250", headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        products = data.get('products', [])
        print(f"Total products: {len(products)}")
        with open('user_store_products.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        for p in products:
            price = p['variants'][0]['price'] if p.get('variants') else '0'
            print(f"- {p.get('title')} (${price}) | Type: {p.get('product_type')} | {len(p.get('images', []))} images")
except Exception as e:
    print("Error on products.json:", e)

print("\nChecking collections.json...")
try:
    req = urllib.request.Request(f"{base_url}/collections.json", headers=headers)
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        collections = data.get('collections', [])
        print(f"Total collections: {len(collections)}")
        with open('user_store_collections.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        for c in collections:
            print(f"- Collection: {c.get('title')} (handle: {c.get('handle')})")
except Exception as e:
    print("Error on collections.json:", e)
