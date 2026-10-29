import os
import zipfile

theme_dir = 'santos-shopify-theme'
output_zip = 'santos-shopify-theme.zip'

if os.path.exists(output_zip):
    os.remove(output_zip)

file_count = 0
total_uncompressed = 0

with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(theme_dir):
        # Exclude .git directory
        if '.git' in root.split(os.sep):
            continue
        for f in files:
            full_path = os.path.join(root, f)
            arcname = os.path.relpath(full_path, theme_dir)
            zf.write(full_path, arcname)
            file_count += 1
            total_uncompressed += os.path.getsize(full_path)

zip_size = os.path.getsize(output_zip)
print(f"Packed {file_count} files into {output_zip}")
print(f"Uncompressed: {total_uncompressed / (1024*1024):.2f} MB")
print(f"Compressed Zip: {zip_size / (1024*1024):.2f} MB")
