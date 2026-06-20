import os

css_path = r"d:\Projects\Portfolio\css\style.css"
html_path = r"d:\Projects\Portfolio\index.html"

# Update CSS
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Typography
css = css.replace("--font-heading: 'Space Grotesk', sans-serif;", "--font-heading: 'Rajdhani', sans-serif;")
css = css.replace("--font-body: 'Inter', sans-serif;", "--font-body: 'Inter', 'Noto Sans JP', sans-serif;")

# Background Grid
bg_old = """body {
    font-family: var(--font-body);
    background-color: var(--bg-dark);
    color: var(--text-main);
    line-height: 1.6;
    overflow-x: hidden;
}"""
bg_new = """body {
    font-family: var(--font-body);
    background-color: var(--bg-dark);
    color: var(--text-main);
    line-height: 1.6;
    overflow-x: hidden;
    background-image: linear-gradient(rgba(167, 139, 250, 0.05) 1px, transparent 1px),
                      linear-gradient(90deg, rgba(167, 139, 250, 0.05) 1px, transparent 1px);
    background-size: 40px 40px;
    background-position: center center;
}"""
css = css.replace(bg_old, bg_new)

# Sharp UI - Remove Border Radius
css = css.replace("border-radius: 4px;", "border-radius: 0;")
css = css.replace("border-radius: 8px;", "border-radius: 0;")
css = css.replace("border-radius: 10px;", "border-radius: 0;")
css = css.replace("border-radius: 12px;", "border-radius: 0;")

# Hard Drop Shadows (Anime Style)
css = css.replace("box-shadow: 0 10px 30px rgba(0,0,0,0.4);", "box-shadow: 6px 6px 0px var(--secondary-accent);")
css = css.replace("box-shadow: 0 5px 20px rgba(0,0,0,0.3);", "box-shadow: 4px 4px 0px var(--secondary-accent);")
css = css.replace("box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 20px rgba(255, 255, 255, 0.1);", "box-shadow: 6px 6px 0px var(--secondary-accent);")
css = css.replace("box-shadow: 0 0 15px rgba(255, 255, 255, 0.1);", "box-shadow: 4px 4px 0px var(--secondary-accent);")
css = css.replace("box-shadow: 0 0 20px var(--primary-accent-glow);", "box-shadow: 6px 6px 0px var(--primary-accent);")

# Add styles for jp-watermark and system-status
additional_styles = """

/* Anime Accents */
.jp-watermark {
    font-family: 'Noto Sans JP', sans-serif;
    opacity: 0.3;
    font-size: 1rem;
    margin-left: 10px;
    letter-spacing: 5px;
    color: var(--secondary-accent);
}
.system-status {
    font-family: 'Rajdhani', sans-serif;
    color: var(--secondary-accent);
    font-size: 1rem;
    margin-top: 30px;
    letter-spacing: 3px;
    opacity: 0.7;
}
.btn-primary, .btn-secondary {
    text-transform: uppercase;
    letter-spacing: 2px;
}
.project-card, .focus-card, .cert-card, .stat-item {
    border: 1px solid var(--secondary-accent);
}
"""
css += additional_styles

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# Update HTML
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Font Links
html = html.replace(
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Space+Grotesk:wght@500;700&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=Rajdhani:wght@500;600;700&family=Noto+Sans+JP:wght@400;700&display=swap" rel="stylesheet">'
)

# Accents
html = html.replace('<p class="greeting">Hello, I\'m</p>', '<p class="greeting">Hello, I\'m <span class="jp-watermark">サイバーセキュリティ</span></p>')

sys_status = """            <div class="hero-cta">
                <a href="#projects" class="btn btn-primary">View My Work</a>
                <a href="#" class="btn btn-secondary"><i class="fas fa-download"></i> Download CV</a>
            </div>
            <div class="system-status">// SYS.ONLINE_</div>"""
            
html = html.replace("""            <div class="hero-cta">
                <a href="#projects" class="btn btn-primary">View My Work</a>
                <a href="#" class="btn btn-secondary"><i class="fas fa-download"></i> Download CV</a>
            </div>""", sys_status)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Anime Aesthetic successfully applied!")
