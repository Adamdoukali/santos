import json

with open('santos_real_products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

for p in products:
    t = p['title'].lower()
    
    if 'robe' in t or 'dress' in t:
        p['category'] = 'ROBES'
    elif 'ensemble' in t or 'blazer' in t or 'combinaison' in t or 'suit' in t:
        p['category'] = 'ENSEMBLES'
    elif 'jeans' in t or 'denim' in t:
        p['category'] = 'JEANS'
    elif 'manteco' in t or 'trench' in t or 'trensh' in t or 'coat' in t or 'manteau' in t or 'doudoune' in t or 'jacket' in t:
        p['category'] = 'MANTEAUX'
    else:
        p['category'] = 'TOPS | BODYS'

    # If it's denim dress, tag it for both
    if 'robe jeans' in t or 'denim' in t:
        p['tags'].append('jeans')
        p['tags'].append('robe')

with open('santos_real_products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print("Updated categories successfully!")
for p in products:
    print(f"- {p['title']} => {p['category']}")
