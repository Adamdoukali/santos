import os
import json
import urllib.request

os.makedirs('assets/images/collections', exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

with open('user_store_collections.json', 'r', encoding='utf-8') as f:
    cols_data = json.load(f)

for c in cols_data.get('collections', []):
    img = c.get('image')
    handle = c.get('handle')
    if img and img.get('src'):
        src = img.get('src')
        ext = src.split('?')[0].split('.')[-1]
        local_filename = f"{handle}.{ext}"
        local_path = os.path.join('assets/images/collections', local_filename)
        try:
            req = urllib.request.Request(src, headers=headers)
            with urllib.request.urlopen(req) as resp, open(local_path, 'wb') as out:
                out.write(resp.read())
            print(f"Downloaded collection image: {local_path}")
        except Exception as e:
            print(f"Failed {handle}: {e}")
