import os
from PIL import Image

# === CONFIG ===
input_folder = "images"
output_folder = "resized"
new_size = (800, 800)  # (width, height)

# === Ensure output folder exists ===
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# === Loop through all files in input folder ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize image
        resized_img = img.resize(new_size)

        # Optional: Convert format (e.g., to JPEG)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

        # Save resized image
        resized_img.save(output_path)

        print(f"✅ Resized and saved: {output_path}")

print("\n🎯 All images have been resized successfully!")
