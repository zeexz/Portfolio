// Wait for DOM to load
document.addEventListener('DOMContentLoaded', () => {
    initLoadingScreen();
    initMobileMenu();
    initStickyNav();
    initScrollReveal();
    initTypedText();
    initProjectFilter();
    initParticlesCanvas();
    initHeroHover();
    initThemeToggle();
    initCursor();
    initCardTilt();
    initMagneticButtons();
    initStatsCounter();
    initBackToTop();
    initParallax();
});

// Mobile Menu Toggle
function initMobileMenu() {
    const menuBtn = document.querySelector('.menu-btn');
    const navLinks = document.querySelector('.nav-links');

    menuBtn.addEventListener('click', () => {
        menuBtn.classList.toggle('active');
        navLinks.classList.toggle('active');
    });

    // Close menu when a link is clicked
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            menuBtn.classList.remove('active');
            navLinks.classList.remove('active');
        });
    });
}

// Sticky Nav & Active Link Highlight
function initStickyNav() {
    const navbar = document.getElementById('navbar');
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');
    let ticking = false;

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                // Sticky Nav
                if (window.scrollY > 50) {
                    navbar.classList.add('scrolled');
                } else {
                    navbar.classList.remove('scrolled');
                }

                // Active Link Highlight
                let current = '';
                sections.forEach(section => {
                    const sectionTop = section.offsetTop;
                    const sectionHeight = section.clientHeight;
                    if (window.scrollY >= (sectionTop - sectionHeight / 3)) {
                        current = section.getAttribute('id');
                    }
                });

                // Scroll Progress
                const scrollProgress = document.getElementById('scroll-progress');
                if (scrollProgress) {
                    const scrollTotal = document.documentElement.scrollHeight - window.innerHeight;
                    const scrollPercent = (window.scrollY / scrollTotal) * 100;
                    scrollProgress.style.width = scrollPercent + '%';
                }

                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${current}`) {
                        link.classList.add('active');
                    }
                });
                ticking = false;
            });
            ticking = true;
        }
    });
}

// Scroll Reveal Animation (Intersection Observer)
function initScrollReveal() {
    const revealElements = document.querySelectorAll('.reveal');

    const revealCallback = (entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Stop observing once revealed
            }
        });
    };

    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealObserver = new IntersectionObserver(revealCallback, revealOptions);

    revealElements.forEach(el => {
        revealObserver.observe(el);
    });
}

// Cyberpunk Scramble Text Effect
function initTypedText() {
    const typedTextSpan = document.querySelector(".typed-text");
    const cursorSpan = document.querySelector(".cursor");
    
    if (cursorSpan) {
        cursorSpan.style.display = "none";
    }

    const textArray = ["Network Security", "Low-Level Programming", "Malware Analysis", "Threat Intelligence"];
    let textArrayIndex = 0;
    const chars = "!<>-_\\\\/[]{}—=+*^?#________";
    
    function scrambleText(newText) {
        let iteration = 0;
        clearInterval(typedTextSpan.interval);
        
        typedTextSpan.interval = setInterval(() => {
            typedTextSpan.innerText = newText
                .split("")
                .map((letter, index) => {
                    if(index < iteration) {
                        return newText[index];
                    }
                    return chars[Math.floor(Math.random() * chars.length)];
                })
                .join("");
            
            if(iteration >= newText.length){ 
                clearInterval(typedTextSpan.interval);
                setTimeout(() => {
                    textArrayIndex = (textArrayIndex + 1) % textArray.length;
                    scrambleText(textArray[textArrayIndex]);
                }, 3000);
            }
            
            iteration += 1 / 3;
        }, 30);
    }
    
    if(textArray.length) {
        setTimeout(() => {
            scrambleText(textArray[textArrayIndex]);
        }, 1000);
    }
}

// Project Filter
function initProjectFilter() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectCards = document.querySelectorAll('.project-card');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            btn.classList.add('active');

            const filterValue = btn.getAttribute('data-filter');

            projectCards.forEach(card => {
                if (filterValue === 'all' || card.getAttribute('data-category') === filterValue) {
                    card.style.display = 'flex';
                    // Trigger reflow to restart animation
                    void card.offsetWidth;
                    card.style.opacity = '1';
                    card.style.transform = 'scale(1)';
                } else {
                    card.style.display = 'none';
                    card.style.opacity = '0';
                    card.style.transform = 'scale(0.8)';
                }
            });
        });
    });
}

// Japanese Alphabet Background Canvas
function initParticlesCanvas() {
    const canvas = document.getElementById('bg-canvas');
    const ctx = canvas.getContext('2d');
    
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    
    let particlesArray = [];
    const numberOfParticles = Math.floor(window.innerWidth / 15);
    const jpChars = "アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズヅブプエェケセテネヘメレヱゲゼデベペオォコソトノホモヨョロゴゾドボポヴッン".split('');
    
    // Theme-aware particle colors
    function getParticleColors() {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        if (isDark) {
            return [
                'rgba(248, 250, 252, 0.5)',
                'rgba(239, 68, 68, 0.7)'
            ];
        }
        return [
            'rgba(0, 0, 0, 0.8)',
            'rgba(220, 38, 38, 0.9)'
        ];
    }
    
    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        init();
    });

    class Letter {
        constructor() {
            // Spawn anywhere initially for immediate effect, heavily biased to top-left
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 3 + 1; // Letter size multiplier
            this.speedX = Math.random() * 1 + 0.5; // Drift RIGHT slowly
            this.speedY = Math.random() * 0.8 + 0.2; // Fall DOWN gently
            this.angle = Math.random() * 360; // Rotation angle
            this.spin = (Math.random() < 0.5 ? -1 : 1) * (Math.random() * 1 + 0.2); // Slower spin
            // Use theme-aware colors
            const colors = getParticleColors();
            this.color = Math.random() > 0.6 ? colors[0] : colors[1];
            this.char = jpChars[Math.floor(Math.random() * jpChars.length)];
        }
        
        update(speedFactor = 1) {
            this.x += (this.speedX + Math.sin(this.angle * Math.PI / 180) * 0.5) * speedFactor; // Gentle sway
            this.y += this.speedY * speedFactor;
            this.angle += this.spin * speedFactor;
            
            // If they fall off screen right or bottom, respawn at the tree (top-left)
            if (this.y > canvas.height + 10 || this.x > canvas.width + 10) {
                // Respawn near the tree branches (top-left 30% of screen)
                this.y = Math.random() * (canvas.height * 0.3) - 20;
                this.x = Math.random() * (canvas.width * 0.3) - 20;
                this.char = jpChars[Math.floor(Math.random() * jpChars.length)];
            }
        }
        
        draw() {
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.rotate(this.angle * Math.PI / 180);
            ctx.fillStyle = this.color;
            ctx.font = `${this.size * 6}px 'Noto Serif JP', serif`;
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(this.char, 0, 0);
            ctx.restore();
        }
    }
    
    function init() {
        particlesArray = [];
        for (let i = 0; i < numberOfParticles; i++) {
            particlesArray.push(new Letter());
        }
    }
    
    let lastTime = 0;
    function animate(currentTime) {
        if (!lastTime) lastTime = currentTime;
        let deltaTime = currentTime - lastTime;
        lastTime = currentTime;
        
        // Cap deltaTime to avoid massive jumps if tab was inactive
        if (deltaTime > 50) deltaTime = 16.6; 
        
        // Target 60fps -> 16.6ms per frame. So speed factor is deltaTime / 16.6
        const speedFactor = deltaTime / 16.6;

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < particlesArray.length; i++) {
            particlesArray[i].update(speedFactor);
            particlesArray[i].draw();
        }
        requestAnimationFrame(animate);
    }
    
    init();
    requestAnimationFrame(animate);
    
    // Update particle colors when theme changes
    window.addEventListener('themechange', () => {
        const colors = getParticleColors();
        particlesArray.forEach(p => {
            p.color = Math.random() > 0.6 ? colors[0] : colors[1];
        });
    });
}

// Hover Hero Section - Nav Link Color Change
function initHeroHover() {
    const heroSection = document.getElementById('hero');
    const navbar = document.getElementById('navbar');
    
    if (heroSection && navbar) {
        heroSection.addEventListener('mouseenter', () => {
            navbar.classList.add('hero-hover');
        });
        
        heroSection.addEventListener('mouseleave', () => {
            navbar.classList.remove('hero-hover');
        });
    }
}

// Theme Toggle
function initThemeToggle() {
    const toggleBtn = document.getElementById('theme-toggle');
    if (!toggleBtn) return;
    
    // Check local storage
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        toggleBtn.innerHTML = '<i class="fas fa-sun"></i>';
    }

    toggleBtn.addEventListener('click', () => {
        let theme = document.documentElement.getAttribute('data-theme');
        if (theme === 'dark') {
            document.documentElement.removeAttribute('data-theme');
            localStorage.setItem('theme', 'light');
            toggleBtn.innerHTML = '<i class="fas fa-moon"></i>';
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
            toggleBtn.innerHTML = '<i class="fas fa-sun"></i>';
        }
        // Notify canvas particles to update colors
        window.dispatchEvent(new CustomEvent('themechange'));
    });
}

// Custom Trailing Cursor
function initCursor() {
    const cursorDot = document.querySelector('.cursor-dot');
    const cursorOutline = document.querySelector('.cursor-outline');
    if (!cursorDot || !cursorOutline) return;

    window.addEventListener('mousemove', (e) => {
        const posX = e.clientX;
        const posY = e.clientY;

        cursorDot.style.left = `${posX}px`;
        cursorDot.style.top = `${posY}px`;

        // Smooth trailing effect
        cursorOutline.animate({
            left: `${posX}px`,
            top: `${posY}px`
        }, { duration: 500, fill: "forwards" });
    });
}

// 3D Card Tilt
function initCardTilt() {
    const cards = document.querySelectorAll('.project-card, .focus-card');
    cards.forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = ((y - centerY) / centerY) * -10;
            const rotateY = ((x - centerX) / centerX) * 10;
            
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = `perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)`;
            card.style.transition = 'transform 0.5s ease';
        });
        
        card.addEventListener('mouseenter', () => {
            card.style.transition = 'none'; // Remove transition for smooth tracking
        });
    });
}

// Magnetic Buttons
function initMagneticButtons() {
    const buttons = document.querySelectorAll('.btn, .social-links a');
    
    buttons.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;
            
            btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
        });
        
        btn.addEventListener('mouseleave', () => {
            btn.style.transform = 'translate(0px, 0px)';
        });
    });
}

// Loading Screen
function initLoadingScreen() {
    const loader = document.getElementById('loading-screen');
    const hackingText = document.querySelector('.hacking-text');
    if (!loader) return;
    
    if (hackingText) {
        const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+";
        let interval = null;
        let iteration = 0;
        
        clearInterval(interval);
        
        interval = setInterval(() => {
            hackingText.innerText = hackingText.innerText
                .split("")
                .map((letter, index) => {
                    if(index < iteration) {
                        return hackingText.dataset.value[index];
                    }
                    return letters[Math.floor(Math.random() * 48)];
                })
                .join("");
            
            if(iteration >= hackingText.dataset.value.length){ 
                clearInterval(interval);
            }
            
            iteration += 1 / 3;
        }, 30);
    }
    
    // Dismiss after animations play
    setTimeout(() => {
        loader.classList.add('hidden');
        // Remove from DOM after transition
        setTimeout(() => {
            loader.remove();
        }, 800);
    }, 2500);
}

// Stats Counter Animation
function initStatsCounter() {
    const statNumbers = document.querySelectorAll('.stat-number[data-target]');
    if (!statNumbers.length) return;
    
    const animateCounter = (el) => {
        const target = parseInt(el.getAttribute('data-target'));
        const suffix = el.getAttribute('data-suffix') || '';
        const duration = 1500; // ms
        const startTime = performance.now();
        
        function update(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            
            // Ease-out cubic
            const eased = 1 - Math.pow(1 - progress, 3);
            const current = Math.floor(eased * target);
            
            el.textContent = current + suffix;
            
            if (progress < 1) {
                requestAnimationFrame(update);
            } else {
                el.textContent = target + suffix;
            }
        }
        
        requestAnimationFrame(update);
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounter(entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    statNumbers.forEach(el => observer.observe(el));
}

// Back to Top Button
function initBackToTop() {
    const btn = document.getElementById('back-to-top');
    if (!btn) return;
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 600) {
            btn.classList.add('visible');
        } else {
            btn.classList.remove('visible');
        }
    });
    
    btn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

// Subtle Parallax on Hero Background
function initParallax() {
    const hero = document.querySelector('.hero');
    if (!hero) return;
    
    let ticking = false;
    window.addEventListener('scroll', () => {
        if (!ticking) {
            requestAnimationFrame(() => {
                const scrollY = window.scrollY;
                const heroHeight = hero.offsetHeight;
                
                if (scrollY <= heroHeight) {
                    // Parallax: tree moves slower than scroll
                    const offset = scrollY * 0.3;
                    hero.style.backgroundPosition = `top ${-offset}px left`;
                }
                ticking = false;
            });
            ticking = true;
        }
    });
}
