import urllib.request
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

base_url = "https://a9xpr3-x0.myshopify.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

with open('user_store_collections.json', 'r', encoding='utf-8') as f:
    cols_data = json.load(f)

for c in cols_data.get('collections', []):
    handle = c.get('handle')
    title = c.get('title')
    url = f"{base_url}/collections/{handle}/products.json"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            prods = data.get('products', [])
            print(f"Collection '{title}' ({handle}): {len(prods)} products")
            for p in prods:
                print(f"   -> {p.get('title')}")
    except Exception as e:
        print(f"Error fetching {handle}: {e}")
