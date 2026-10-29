import json
import sys

with open('santos_real_products.json', 'r', encoding='utf-8') as f:
    products = json.load(f)

color_maps = {
    'MANTECO ORIGINALLY ❤️‍🔥': [
        {'name': 'Noir', 'hex': '#1a1a1a', 'img_idx': 0},
        {'name': 'Camel', 'hex': '#9e6d42', 'img_idx': 1},
        {'name': 'Kaki', 'hex': '#4b5320', 'img_idx': 2}
    ],
    'Trensh original': [
        {'name': 'Camel', 'hex': '#b89069', 'img_idx': 0},
        {'name': 'Kaki Chic', 'hex': '#5a6344', 'img_idx': 1},
        {'name': 'Noir', 'hex': '#111111', 'img_idx': 2}
    ],
    'ENSEMBLE SANTOS': [
        {'name': 'Red', 'hex': '#a82020', 'img_idx': 0},
        {'name': 'Jaune', 'hex': '#d4a017', 'img_idx': 1}
    ],
    'BLAZER SURPIQÛRES CONTRASTE ZW COLLECTION LIMITED EDITION': [
        {'name': 'Noir', 'hex': '#111111', 'img_idx': 0},
        {'name': 'somo yamo', 'hex': '#c67d63', 'img_idx': 1},
        {'name': 'Navy', 'hex': '#1d2a44', 'img_idx': 2}
    ],
    'Regular Fit Wool Like Midi Length Belted Coat For Women santos': [
        {'name': 'Anthracite', 'hex': '#4a4a4a', 'img_idx': 0},
        {'name': 'Noir', 'hex': '#181818', 'img_idx': 1},
        {'name': 'Camel', 'hex': '#aa7a4a', 'img_idx': 2}
    ],
    'TRUE AVENUE BLACK VALE JACKET SANTOS': [
        {'name': 'Noir Cuir', 'hex': '#1c1c1c', 'img_idx': 0},
        {'name': 'Chocolat', 'hex': '#3b2219', 'img_idx': 1}
    ],
    "Women's Trench Coat Fleece-Lined Mid-length Jacket santos magic": [
        {'name': 'Beige Sable', 'hex': '#d8c29d', 'img_idx': 0},
        {'name': 'Kaki Fumé', 'hex': '#636854', 'img_idx': 1},
        {'name': 'Noir', 'hex': '#212121', 'img_idx': 2}
    ],
    'Trench Kaki Chic Original': [
        {'name': 'Kaki Chic', 'hex': '#4d5338', 'img_idx': 0},
        {'name': 'Beige', 'hex': '#c2b69d', 'img_idx': 1}
    ],
    'Combinaison Velvet Gold Luxe': [
        {'name': 'Velours Doré', 'hex': '#a88942', 'img_idx': 0},
        {'name': 'Noir', 'hex': '#111111', 'img_idx': 1}
    ],
    'Manteco, manteau long ceinturé ultra chic': [
        {'name': 'Noir Imperial', 'hex': '#151515', 'img_idx': 0},
        {'name': 'Camel Royal', 'hex': '#8b5a2b', 'img_idx': 1}
    ],
    'Doudoune Original France': [
        {'name': 'Noir Laqué', 'hex': '#1a1a1a', 'img_idx': 0},
        {'name': 'Blanc Neige', 'hex': '#eeeeee', 'img_idx': 1}
    ],
    'Grace Buckle Detail Black Midi Shirt Dress': [
        {'name': 'Noir Intense', 'hex': '#111111', 'img_idx': 0},
        {'name': 'Marine', 'hex': '#18263b', 'img_idx': 1}
    ],
    'ENSEMBLE LIN SAHARA': [
        {'name': 'Green', 'hex': '#4e6b50', 'img_idx': 0},
        {'name': 'Navy', 'hex': '#1d2a44', 'img_idx': 1},
        {'name': 'somo yamo', 'hex': '#c87a64', 'img_idx': 2}
    ],
    'Robe jeans new collection 2026': [
        {'name': 'Bleu Ciel', 'hex': '#789bbe', 'img_idx': 0},
        {'name': 'Blue Denim', 'hex': '#2b4a72', 'img_idx': 1}
    ],
    'Blazer Ensemble Melange De Crep Santos1 Collection': [
        {'name': 'Pink', 'hex': '#e8a5b8', 'img_idx': 0},
        {'name': 'White', 'hex': '#f5f5f5', 'img_idx': 1},
        {'name': 'Black', 'hex': '#111111', 'img_idx': 2},
        {'name': 'Beige', 'hex': '#d6c4a8', 'img_idx': 3},
        {'name': 'Kaki', 'hex': '#556b2f', 'img_idx': 4},
        {'name': 'Bleu Ciel', 'hex': '#87ceeb', 'img_idx': 0},
        {'name': 'somo yamo', 'hex': '#c87a64', 'img_idx': 1}
    ]
}

compare_prices = {
    'MANTECO ORIGINALLY ❤️‍🔥': 990.0,
    'Trensh original': 850.0,
    'ENSEMBLE SANTOS': 800.0,
    'BLAZER SURPIQÛRES CONTRASTE ZW COLLECTION LIMITED EDITION': 700.0,
    'Regular Fit Wool Like Midi Length Belted Coat For Women santos': 890.0,
    'TRUE AVENUE BLACK VALE JACKET SANTOS': 950.0,
    "Women's Trench Coat Fleece-Lined Mid-length Jacket santos magic": 550.0,
    'Trench Kaki Chic Original': 750.0,
    'Combinaison Velvet Gold Luxe': 750.0,
    'Manteco, manteau long ceinturé ultra chic': 750.0,
    'Doudoune Original France': 650.0,
    'Grace Buckle Detail Black Midi Shirt Dress': 450.0,
    'ENSEMBLE LIN SAHARA': 590.0,
    'Robe jeans new collection 2026': 490.0,
    'Blazer Ensemble Melange De Crep Santos1 Collection': 690.0
}

for p in products:
    title = p['title']
    if title in compare_prices:
        p['compare_at_price'] = compare_prices[title]
    else:
        p['compare_at_price'] = round(p['price'] * 1.3, 0)
    
    if title in color_maps:
        p['colors_data'] = color_maps[title]
        p['colors'] = [c['name'] for c in color_maps[title]]
    else:
        p['colors_data'] = []

with open('santos_real_products.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, indent=2, ensure_ascii=False)

print('santos_real_products.json successfully updated!')
