import os
import shutil

# Copy image
src = r"C:\Users\prabh\.gemini\antigravity-ide\brain\adb04423-e3e3-49f9-8334-980870c59758\sakura_top_left_bg_1781964743964.png"
dst = r"d:\Projects\Portfolio\assets\sakura_top_left_bg.png"
shutil.copyfile(src, dst)

css_path = r"d:\Projects\Portfolio\css\style.css"
js_path = r"d:\Projects\Portfolio\js\main.js"

# Update CSS
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

hero_old = """/* Hero Samurai Art Background */
.hero {
    background-image: url('../assets/pure_samurai_bg.png');
    background-size: contain;
    background-position: right 10% bottom;
    background-repeat: no-repeat;
    opacity: 1;
}"""
hero_new = """/* Hero Top Left Tree Background */
.hero {
    background-image: url('../assets/sakura_top_left_bg.png');
    background-size: 40%;
    background-position: top left;
    background-repeat: no-repeat;
    opacity: 0.9;
}"""
css = css.replace(hero_old, hero_new)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

# Update JS Petal logic
with open(js_path, "r", encoding="utf-8") as f:
    js = f.read()

# Replace the particle physics in main.js
old_petal_class = """    class Petal {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 3 + 1; // Petal size
            this.speedX = Math.random() * 2 - 1; // Drift left/right
            this.speedY = Math.random() * 1.5 + 0.5; // Fall down
            this.angle = Math.random() * 360; // Rotation angle
            this.spin = (Math.random() < 0.5 ? -1 : 1) * (Math.random() * 2 + 0.5); // Spin speed
            // Crimson red and crisp white colors for Sakura theme
            this.color = Math.random() > 0.6 ? 'rgba(0, 0, 0, 0.8)' : 'rgba(220, 38, 38, 0.9)';
        }
        
        update() {
            this.x += this.speedX + Math.sin(this.angle * Math.PI / 180) * 0.5; // Gentle sway
            this.y += this.speedY;
            this.angle += this.spin;
            
            // Loop back to top
            if (this.y > canvas.height + 10) {
                this.y = -10;
                this.x = Math.random() * canvas.width;
            }
            if (this.x > canvas.width + 10) this.x = -10;
            else if (this.x < -10) this.x = canvas.width + 10;
        }"""

new_petal_class = """    class Petal {
        constructor() {
            // Spawn anywhere initially for immediate effect, heavily biased to top-left
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 3 + 1; // Petal size
            this.speedX = Math.random() * 2 + 1; // Drift RIGHT (away from tree)
            this.speedY = Math.random() * 1.5 + 0.5; // Fall DOWN
            this.angle = Math.random() * 360; // Rotation angle
            this.spin = (Math.random() < 0.5 ? -1 : 1) * (Math.random() * 2 + 0.5); // Spin speed
            // Crimson red and crisp black colors for Sakura theme
            this.color = Math.random() > 0.6 ? 'rgba(0, 0, 0, 0.8)' : 'rgba(220, 38, 38, 0.9)';
        }
        
        update() {
            this.x += this.speedX + Math.sin(this.angle * Math.PI / 180) * 0.5; // Gentle sway
            this.y += this.speedY;
            this.angle += this.spin;
            
            // If they fall off screen right or bottom, respawn at the tree (top-left)
            if (this.y > canvas.height + 10 || this.x > canvas.width + 10) {
                // Respawn near the tree branches (top-left 30% of screen)
                this.y = Math.random() * (canvas.height * 0.3) - 20;
                this.x = Math.random() * (canvas.width * 0.3) - 20;
            }
        }"""

js = js.replace(old_petal_class, new_petal_class)

with open(js_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Top Left Tree & Petal Wind applied successfully!")
