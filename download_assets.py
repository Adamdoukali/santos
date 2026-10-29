import os
import re
import urllib.request
import urllib.parse

os.makedirs('assets/images', exist_ok=True)
os.makedirs('assets/videos', exist_ok=True)

with open(r'C:\Users\Claro\.gemini\antigravity-ide\brain\e4e2c726-8d47-4f63-b641-37c2eedfb73f\.system_generated\steps\9\content.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract image urls
img_urls = set(re.findall(r'//www\.balmoralrunning\.com/cdn/shop/files/[^"\s,\'\)]+', text))

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url_map = {}

print(f"Found {len(img_urls)} unique image URLs to cache")

for u in sorted(img_urls):
    full_url = 'https:' + u
    clean_name = u.split('/')[-1].split('?')[0]
    local_path = os.path.join('assets/images', clean_name)
    url_map[u] = 'assets/images/' + clean_name
    if not os.path.exists(local_path):
        try:
            req = urllib.request.Request(full_url, headers=headers)
            with urllib.request.urlopen(req) as resp, open(local_path, 'wb') as out:
                out.write(resp.read())
            print(f"Downloaded: {clean_name}")
        except Exception as e:
            print(f"Error {clean_name}: {e}")

# Also download the secondary video in about us if present
sec_video_url = "https://www.balmoralrunning.com/cdn/shop/videos/c/vp/c96a1942b1894cf18a35d6da49aee5a7/c96a1942b1894cf18a35d6da49aee5a7.HD-1080p-7.2Mbps-81646476.mp4"
sec_video_local = "assets/videos/about-secondary.mp4"
if not os.path.exists(sec_video_local):
    try:
        print("Downloading secondary video...")
        req = urllib.request.Request(sec_video_url, headers=headers)
        with urllib.request.urlopen(req) as resp, open(sec_video_local, 'wb') as out:
            out.write(resp.read())
        print("Secondary video downloaded!")
    except Exception as e:
        print("Error downloading secondary video:", e)

print("Done caching assets!")
