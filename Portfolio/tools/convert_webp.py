import os
from PIL import Image

assets_dir = r"d:\Projects\Portfolio\assets"

def convert_to_webp(directory):
    for filename in os.listdir(directory):
        if filename.lower().endswith(".png"):
            png_path = os.path.join(directory, filename)
            webp_path = os.path.join(directory, os.path.splitext(filename)[0] + ".webp")
            
            # Open image and convert
            try:
                with Image.open(png_path) as img:
                    img.save(webp_path, "WEBP", quality=80)
                    print(f"Converted {filename} to WebP.")
                # Optionally, you can delete the original png to save space, but we'll keep it for now.
            except Exception as e:
                print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    convert_to_webp(assets_dir)
