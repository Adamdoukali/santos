import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('santos_real_products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for p in products:
    print(f"{p['title']}:")
    print(f"  Colors: {p.get('colors')}")
    print(f"  Sizes: {p.get('sizes')}")
    print(f"  Desc: {p.get('desc')[:80]}...")
