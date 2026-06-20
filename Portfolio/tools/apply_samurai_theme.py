import shutil
import os

# Copy image
src = r"C:\Users\prabh\.gemini\antigravity-ide\brain\adb04423-e3e3-49f9-8334-980870c59758\samurai_hero_bg_1781964287070.png"
dst = r"d:\Projects\Portfolio\assets\samurai_hero_bg.png"
shutil.copyfile(src, dst)

css_path = r"d:\Projects\Portfolio\css\style.css"
html_path = r"d:\Projects\Portfolio\index.html"

# Update HTML
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Update fonts
html = html.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Rajdhani:wght@500;600;700&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800;900&family=Noto+Serif+JP:wght@400;700;900&display=swap" rel="stylesheet">'
)

# Update Text Accents
html = html.replace('サイバーセキュリティ・スペシャリスト', 'サイバー武士')
html = html.replace('サイバーセキュリティ', '武士道')
html = html.replace('// SYS.ONLINE_', '[ 道 ] THE WAY OF THE WARRIOR')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

# Update CSS
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Update fonts
css = css.replace("--font-heading: 'Rajdhani', sans-serif;", "--font-heading: 'Cinzel', serif;")
css = css.replace("--font-body: 'Inter', 'Noto Sans JP', sans-serif;", "--font-body: 'Noto Serif JP', serif;")

# Remove CRT Scanline
crt_block = """/* CRT Scanlines Overlay */
body::after {
    content: " ";
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background: linear-gradient(rgba(255, 255, 255, 0) 50%, rgba(0, 0, 0, 0.05) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.02), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.02));
    z-index: 9999;
    background-size: 100% 2px, 3px 100%;
    pointer-events: none;
}"""
css = css.replace(crt_block, "/* CRT Scanlines Removed for Samurai Theme */")

# Update Hero Background
hero_old = """/* Hero Anime Sakura Art Background */
.hero {
    background-image: url('../assets/sakura_tree_bg.png');
    background-size: auto 90%; /* Keep tree proportional, fit height */
    background-position: right 5% bottom; /* Push to the right side */
    background-repeat: no-repeat;
    opacity: 0.8; /* Subtle transparency so it doesn't block text */
}"""
hero_new = """/* Hero Samurai Art Background */
.hero {
    background-image: url('../assets/samurai_hero_bg.png');
    background-size: auto 90%;
    background-position: right 5% bottom;
    background-repeat: no-repeat;
    opacity: 0.9;
}"""
css = css.replace(hero_old, hero_new)

# Update Vertical Font Family
css = css.replace("font-family: 'Noto Sans JP', sans-serif;", "font-family: 'Noto Serif JP', serif;")

# Add asymmetric cut borders
additional_css = """
/* Samurai Slash Styling */
.project-card, .focus-card, .cert-card, .stat-item {
    border-radius: 20px 0 20px 0;
}
.btn {
    border-radius: 10px 0 10px 0;
}
"""
css += additional_css

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("Samurai theme applied successfully!")
