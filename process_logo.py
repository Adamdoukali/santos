from PIL import Image
import numpy as np

src_path = r"C:\Users\Claro\.gemini\antigravity-ide\brain\e4e2c726-8d47-4f63-b641-37c2eedfb73f\.user_uploaded\media_1792087331721.jpg"
img = Image.open(src_path).convert("RGBA")
data = np.array(img, dtype=np.float32)

r, g, b, a = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
# brightness: 0 for black, 255 for white
brightness = 0.299 * r + 0.587 * g + 0.114 * b

# Alpha calculation: black pixels should be fully opaque (255), white pixels fully transparent (0)
# smooth transition for anti-aliasing
alpha = 255.0 - brightness
# clip low noise
alpha = np.where(alpha < 20, 0, alpha)
# normalize
alpha = np.clip((alpha / 240.0) * 255.0, 0, 255).astype(np.uint8)

black_logo = np.zeros((data.shape[0], data.shape[1], 4), dtype=np.uint8)
black_logo[:, :, 0] = 17  # rich near-black
black_logo[:, :, 1] = 17
black_logo[:, :, 2] = 17
black_logo[:, :, 3] = alpha

non_zero = np.where(alpha > 15)
if len(non_zero[0]) > 0:
    min_y, max_y = int(np.min(non_zero[0])), int(np.max(non_zero[0]))
    min_x, max_x = int(np.min(non_zero[1])), int(np.max(non_zero[1]))
    pad = 12
    min_y = max(0, min_y - pad)
    max_y = min(data.shape[0], max_y + pad)
    min_x = max(0, min_x - pad)
    max_x = min(data.shape[1], max_x + pad)
    
    black_crop = black_logo[min_y:max_y, min_x:max_x]
    Image.fromarray(black_crop).save("santos-logo-black.png")
    
    white_logo = np.zeros_like(black_crop)
    white_logo[:, :, 0] = 255
    white_logo[:, :, 1] = 255
    white_logo[:, :, 2] = 255
    white_logo[:, :, 3] = black_crop[:, :, 3]
    Image.fromarray(white_logo).save("santos-logo-white.png")
    
    # Also save original uploaded copy as santos-logo-orig.jpg
    Image.open(src_path).save("santos-logo-orig.jpg")
    print(f"SUCCESS: Logo processed: width={max_x-min_x}, height={max_y-min_y}")
else:
    print("FAILED to find logo pixels")
