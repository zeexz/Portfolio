import os
import shutil

# Copy the light sakura tree image
src = r"C:\Users\prabh\.gemini\antigravity-ide\brain\adb04423-e3e3-49f9-8334-980870c59758\sakura_tree_light_bg_1781964131879.png"
dst = r"d:\Projects\Portfolio\assets\sakura_tree_bg.png"
shutil.copyfile(src, dst)

css_path = r"d:\Projects\Portfolio\css\style.css"
js_path = r"d:\Projects\Portfolio\js\main.js"

# Update CSS
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Variables
old_vars = """    /* Color Palette - Crimson Anime Theme (Akira/Persona) */
    --bg-dark: #0a0a0a; /* Pure Dark */
    --bg-card: rgba(20, 20, 20, 0.8); /* Dark Cards */
    --primary-accent: #ffffff; /* Crisp White */
    --primary-accent-glow: rgba(220, 38, 38, 0.6); /* Crimson Glow */
    --secondary-accent: #dc2626; /* Crimson Red Accent */
    --text-main: #ffffff;
    --text-muted: #a3a3a3;"""

new_vars = """    /* Color Palette - Light Manga Theme */
    --bg-dark: #ffffff; /* Pure White */
    --bg-card: rgba(250, 250, 250, 0.9); /* Light Cards */
    --primary-accent: #000000; /* Crisp Black */
    --primary-accent-glow: rgba(0, 0, 0, 0.15); /* Black Glow */
    --secondary-accent: #dc2626; /* Crimson Red Accent */
    --text-main: #000000;
    --text-muted: #4b5563;"""
css = css.replace(old_vars, new_vars)
css = css.replace("--glass-border: 1px solid rgba(255, 255, 255, 0.08);", "--glass-border: 1px solid rgba(0, 0, 0, 0.15);")

# Name gradient
css = css.replace("linear-gradient(to right, #ffffff, #dc2626)", "linear-gradient(to right, #000000, #dc2626)")

# Grid overlay (body)
css = css.replace("linear-gradient(rgba(167, 139, 250, 0.05) 1px", "linear-gradient(rgba(0, 0, 0, 0.05) 1px")

# Footer and Navbar backgrounds
css = css.replace("background: rgba(10, 10, 10, 0.9);", "background: rgba(255, 255, 255, 0.9);")
css = css.replace("border-top: 1px solid rgba(255, 255, 255, 0.05);", "border-top: 1px solid rgba(0, 0, 0, 0.1);")

# Vertical text
css = css.replace("color: rgba(255, 255, 255, 0.015);", "color: rgba(0, 0, 0, 0.03);")

# Scanline effect overlay (make it lighter)
css = css.replace("background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));", 
                  "background: linear-gradient(rgba(255, 255, 255, 0) 50%, rgba(0, 0, 0, 0.05) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.02), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.02));")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# Update JS (Particle colors)
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

js = js.replace("'rgba(255, 255, 255, 0.7)' : 'rgba(220, 38, 38, 0.8)'", "'rgba(0, 0, 0, 0.8)' : 'rgba(220, 38, 38, 0.9)'")

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Light Manga theme applied successfully!")
