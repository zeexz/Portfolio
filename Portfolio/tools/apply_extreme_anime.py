import os

css_path = r"d:\Projects\Portfolio\css\style.css"
html_path = r"d:\Projects\Portfolio\index.html"

# Extreme Anime CSS
extreme_styles = """
/* EXTREME ANIME STYLING OVERRIDES */

/* CRT Scanlines Overlay */
body::after {
    content: " ";
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.25) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.06), rgba(0, 255, 0, 0.02), rgba(0, 0, 255, 0.06));
    z-index: 9999;
    background-size: 100% 2px, 3px 100%;
    pointer-events: none;
}

/* Giant Vertical Japanese Watermark */
.bg-vertical-text {
    position: fixed;
    right: 3%;
    top: -5%;
    bottom: 0;
    writing-mode: vertical-rl;
    text-orientation: upright;
    font-family: 'Noto Sans JP', sans-serif;
    font-size: 15rem;
    font-weight: 900;
    color: rgba(255, 255, 255, 0.015);
    z-index: -2;
    pointer-events: none;
    line-height: 1;
    white-space: nowrap;
    overflow: hidden;
    user-select: none;
}

/* Skewed Action Titles */
.section-title h2, .name, .role, .btn {
    transform: skewX(-10deg);
}

/* Hero Anime Art Background */
.hero {
    background-image: url('../assets/anime_hero_bg.png');
    background-size: 40%;
    background-position: right center;
    background-repeat: no-repeat;
    background-blend-mode: luminosity;
    opacity: 0.9;
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(extreme_styles)


# HTML updates
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Insert the vertical text div right after opening body tag
body_insert = """<body>
    <!-- Massive Anime Vertical Watermark -->
    <div class="bg-vertical-text">サイバーセキュリティ・スペシャリスト</div>"""

html = html.replace("<body>", body_insert)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Extreme Anime styles applied successfully!")
