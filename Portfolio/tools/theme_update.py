import os

css_path = r"d:\Projects\Portfolio\css\style.css"
js_path = r"d:\Projects\Portfolio\js\main.js"

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# CSS Replacements
css = css.replace("Midnight Blue & Gold", "Anime Manga Theme")
css = css.replace("#070913", "#050505")
css = css.replace("rgba(15, 23, 42", "rgba(20, 20, 20")
css = css.replace("#d4af37", "#ffffff")
css = css.replace("rgba(212, 175, 55", "rgba(255, 255, 255")
css = css.replace("#3b82f6", "#e2e8f0")
css = css.replace("rgba(59, 130, 246", "rgba(226, 232, 240")
css = css.replace("#f1f5f9", "#ffffff")
css = css.replace("#94a3b8", "#a3a3a3")
css = css.replace("rgba(7, 9, 19", "rgba(10, 10, 10")
css = css.replace("filter: grayscale(20%) contrast(1.1);", "filter: grayscale(100%) contrast(1.2);")
css = css.replace("filter: grayscale(0) contrast(1);", "filter: grayscale(50%) contrast(1.1);")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# JS Replacements
js = js.replace("Primary gold and subtle blue colors", "White and light gray colors for anime theme")
js = js.replace("'rgba(59, 130, 246, 0.4)' : 'rgba(212, 175, 55, 0.4)'", "'rgba(255, 255, 255, 0.4)' : 'rgba(200, 200, 200, 0.4)'")
js = js.replace("rgba(212, 175, 55", "rgba(255, 255, 255")

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Theme updated successfully!")
