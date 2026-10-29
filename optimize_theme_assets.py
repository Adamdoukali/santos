import os
import shutil
from PIL import Image

src_dir = "assets/images/santos_products"
dst_dir = "santos-shopify-theme/assets"

os.makedirs(dst_dir, exist_ok=True)

files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

print(f"Found {len(files)} files in {src_dir}")

# We will optimize key representative images for featured products and collections
for fname in files:
    src_path = os.path.join(src_dir, fname)
    dst_path = os.path.join(dst_dir, fname)
    
    # Check if file is already there
    if os.path.exists(dst_path):
        continue
        
    try:
        with Image.open(src_path) as img:
            # Resize if very large (> 1600px width/height)
            max_size = (1600, 1600)
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            
            # Save optimized
            if fname.lower().endswith(('.jpg', '.jpeg')):
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                img.save(dst_path, 'JPEG', quality=85, optimize=True)
            elif fname.lower().endswith('.png'):
                img.save(dst_path, 'PNG', optimize=True)
            elif fname.lower().endswith('.webp'):
                img.save(dst_path, 'WEBP', quality=85)
        print(f"Optimized & copied: {fname}")
    except Exception as e:
        print(f"Error optimizing {fname}: {e}, falling back to copy")
        shutil.copy2(src_path, dst_path)

print("Theme assets populated successfully!")
