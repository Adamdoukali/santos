import os
import json
import urllib.request
import re

os.makedirs('assets/images', exist_ok=True)

with open('balmoral_products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

products = data.get('products', [])
print(f"Processing {len(products)} products...")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

santos_catalog = []

for p in products:
    title = p.get('title', '').replace('\ufffd', 'ô').replace('Vendme', 'Vendôme')
    handle = p.get('handle', '')
    product_type = p.get('product_type', 'General')
    body_html = p.get('body_html', '')
    # Strip HTML tags from description
    clean_desc = re.sub(r'<[^>]+>', ' ', body_html).strip() if body_html else f"Crafted with signature Santos performance textiles. Designed for resilience, movement, and effortless daily wear."
    clean_desc = ' '.join(clean_desc.split())
    # remove Balmoral mentions in description
    clean_desc = clean_desc.replace('Balmoral', 'Santos').replace('balmoral', 'santos')

    variants = p.get('variants', [])
    price = float(variants[0].get('price', 0)) if variants else 0
    
    # Process images
    images = p.get('images', [])
    local_imgs = []
    
    for idx, img in enumerate(images):
        src = img.get('src', '')
        if not src:
            continue
        clean_filename = src.split('/')[-1].split('?')[0]
        local_path = os.path.join('assets/images', clean_filename)
        
        if not os.path.exists(local_path):
            try:
                req = urllib.request.Request(src, headers=headers)
                with urllib.request.urlopen(req) as resp, open(local_path, 'wb') as out:
                    out.write(resp.read())
                print(f"Downloaded: {clean_filename}")
            except Exception as e:
                print(f"Error downloading {clean_filename}: {e}")
                
        local_imgs.append('assets/images/' + clean_filename)
        if idx >= 3: # Keep up to 4 images per product
            break

    # Color options
    options = p.get('options', [])
    colors = []
    for opt in options:
        if opt.get('name', '').lower() in ['color', 'colour', 'couleur']:
            colors = opt.get('values', [])
            break

    santos_catalog.append({
        'id': p.get('id'),
        'handle': handle,
        'name': title,
        'type': product_type,
        'price': price,
        'img': local_imgs[0] if local_imgs else 'assets/images/Balaclava_Black_Main_1024x.jpg',
        'images': local_imgs,
        'colors': colors,
        'desc': clean_desc
    })

with open('santos_catalog.json', 'w', encoding='utf-8') as f:
    json.dump(santos_catalog, f, indent=2, ensure_ascii=False)

print(f"Successfully created santos_catalog.json with {len(santos_catalog)} products!")
