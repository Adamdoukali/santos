import os
import json
import urllib.request
import re

os.makedirs('assets/images/santos_products', exist_ok=True)

with open('user_store_products.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

products = data.get('products', [])
print(f"Downloading images for {len(products)} Santos products...")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

processed_products = []

for p in products:
    title = p.get('title')
    handle = p.get('handle')
    body_html = p.get('body_html', '')
    clean_desc = re.sub(r'<[^>]+>', ' ', body_html).strip() if body_html else f"Pièce signature de la collection Santos Haute Couture. Confectionnée avec des tissus d'exception pour une silhouette raffinée et intemporelle."
    clean_desc = ' '.join(clean_desc.split())
    
    variants = p.get('variants', [])
    price_val = 0
    if variants:
        try:
            price_val = float(variants[0].get('price', 0))
        except:
            price_val = 499.0
    if price_val == 0:
        # Give realistic luxury pricing if placeholder was 0
        if 'manteco' in title.lower() or 'wool' in title.lower():
            price_val = 750.0
        elif 'combinaison' in title.lower():
            price_val = 620.0
        else:
            price_val = 499.0

    # Categorization based on handle, title, or type
    t_lower = title.lower()
    if 'ensemble' in t_lower or 'suit' in t_lower:
        category = 'ENSEMBLES'
    elif 'robe' in t_lower or 'dress' in t_lower or 'shirt dress' in t_lower:
        category = 'ROBES'
    elif 'jeans' in t_lower or 'denim' in t_lower:
        category = 'JEANS'
    elif 'manteco' in t_lower or 'trench' in t_lower or 'coat' in t_lower or 'manteau' in t_lower or 'doudoune' in t_lower or 'jacket' in t_lower:
        category = 'MANTEAUX & COATS'
    else:
        category = 'TOPS | BODYS'

    # Download images
    images = p.get('images', [])
    local_images = []
    
    for idx, img_obj in enumerate(images):
        src = img_obj.get('src', '')
        if not src:
            continue
        clean_filename = f"{p['id']}_{idx}_" + src.split('/')[-1].split('?')[0]
        local_path = os.path.join('assets/images/santos_products', clean_filename)
        
        if not os.path.exists(local_path):
            try:
                req = urllib.request.Request(src, headers=headers)
                with urllib.request.urlopen(req) as resp, open(local_path, 'wb') as out:
                    out.write(resp.read())
                print(f"Downloaded: {clean_filename}")
            except Exception as e:
                print(f"Error {clean_filename}: {e}")
                
        local_images.append('assets/images/santos_products/' + clean_filename)

    # Options (Colors, Sizes)
    color_vals = []
    size_vals = []
    for opt in p.get('options', []):
        opt_name = opt.get('name', '').lower()
        if 'couleur' in opt_name or 'color' in opt_name:
            color_vals = opt.get('values', [])
        elif 'taille' in opt_name or 'size' in opt_name:
            size_vals = opt.get('values', [])

    processed_products.append({
        'id': p.get('id'),
        'title': title,
        'handle': handle,
        'category': category,
        'price': price_val,
        'price_formatted': f"${price_val:.2f} CAD",
        'img': local_images[0] if local_images else 'assets/images/santos_products/placeholder.jpg',
        'images': local_images,
        'colors': color_vals,
        'sizes': size_vals if size_vals else ['S', 'M', 'L', 'XL'],
        'desc': clean_desc,
        'tags': p.get('tags', [])
    })

with open('santos_real_products.json', 'w', encoding='utf-8') as f:
    json.dump(processed_products, f, indent=2, ensure_ascii=False)

print(f"Successfully processed {len(processed_products)} real Santos products!")
