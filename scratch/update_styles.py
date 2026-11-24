import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update Hero Visual section
hero_target = """.hero-visual-frame {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 480px;
}

.hero-img-wrap {
  position: relative;
  display: flex;
  justify-content: center;
  filter: drop-shadow(0 20px 35px rgba(0, 0, 0, 0.55));
}"""

hero_replacement = """.hero-visual-frame {
  position: relative;
  z-index: 2;
  width: 100%;
  max-width: 480px;
  animation: heroLevitate 6s ease-in-out infinite alternate;
  perspective: 1000px;
}

@keyframes heroLevitate {
  0% {
    transform: translateY(0px) rotate(0deg);
  }
  100% {
    transform: translateY(-12px) rotate(0.6deg);
  }
}

.hero-img-wrap {
  position: relative;
  display: flex;
  justify-content: center;
  filter: drop-shadow(0 20px 35px rgba(0, 0, 0, 0.55));
  border-radius: 24px;
  overflow: hidden;
}

.hero-img-wrap::after {
  content: '';
  position: absolute;
  top: -60%;
  left: -80%;
  width: 140%;
  height: 220%;
  background: linear-gradient(
    105deg,
    transparent 35%,
    rgba(255, 255, 255, 0.1) 46%,
    rgba(244, 225, 226, 0.28) 50%,
    rgba(255, 255, 255, 0.1) 54%,
    transparent 65%
  );
  transform: rotate(25deg);
  pointer-events: none;
  z-index: 5;
  animation: shimmerSweep 7s infinite ease-in-out 1s;
}"""

if hero_target in css:
    css = css.replace(hero_target, hero_replacement)
    print("Hero updated successfully")
else:
    print("Hero target not found, trying regex")
    css = re.sub(
        r'\.hero-visual-frame\s*\{[^}]*\}\s*\.hero-img-wrap\s*\{[^}]*\}',
        hero_replacement,
        css
    )
    print("Hero updated via regex")

# 2. Update About Card Frame
about_target = """.about-card-frame {
  background: var(--grad-card);
  border: 1px solid var(--border-card);
  border-radius: var(--radius-lg);
  padding: 32px;
  box-shadow: 0 20px 45px rgba(0, 0, 0, 0.35);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.about-img-wrap {
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid rgba(214, 145, 174, 0.3);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}"""

about_replacement = """.about-card-frame {
  background: var(--grad-card);
  border: 1px solid var(--border-card);
  border-radius: var(--radius-lg);
  padding: 32px;
  box-shadow: 0 20px 45px rgba(0, 0, 0, 0.35);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  display: flex;
  flex-direction: column;
  gap: 24px;
  animation: aboutLevitate 7s ease-in-out infinite alternate 0.5s;
  perspective: 1000px;
  transition: var(--transition);
}

.about-card-frame:hover {
  transform: translateY(-8px) scale(1.015);
  box-shadow: 0 25px 55px rgba(0, 0, 0, 0.45), var(--glow-accent);
  border-color: var(--border-card-hover);
}

@keyframes aboutLevitate {
  0% {
    transform: translateY(0px);
  }
  100% {
    transform: translateY(-8px);
  }
}

.about-img-wrap {
  position: relative;
  border-radius: var(--radius-md);
  overflow: hidden;
  border: 1px solid rgba(214, 145, 174, 0.3);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
}

.about-img-wrap::after {
  content: '';
  position: absolute;
  top: -60%;
  left: -80%;
  width: 140%;
  height: 220%;
  background: linear-gradient(
    105deg,
    transparent 35%,
    rgba(255, 255, 255, 0.08) 46%,
    rgba(244, 225, 226, 0.2) 50%,
    rgba(255, 255, 255, 0.08) 54%,
    transparent 65%
  );
  transform: rotate(25deg);
  pointer-events: none;
  z-index: 5;
  animation: shimmerSweep 8s infinite ease-in-out 2s;
}"""

if about_target in css:
    css = css.replace(about_target, about_replacement)
    print("About updated successfully")
else:
    print("About target not found, trying regex")
    css = re.sub(
        r'\.about-card-frame\s*\{[^}]*\}\s*\.about-img-wrap\s*\{[^}]*\}',
        about_replacement,
        css
    )
    print("About updated via regex")

# 3. Update Registration Section
reg_pattern = r'/\* =+\s*13\. Registration Section \(#registration\)\s*=+\s*\*/.*?\.agency-id-callout\s*\{[^}]*\}'

reg_replacement = """/* ==========================================================================
   13. Registration Section (#registration)
   ========================================================================== */
.registration-timeline-wrap {
  max-width: 820px;
  margin: 0 auto;
  position: relative;
}

.reg-steps-flow {
  display: flex;
  flex-direction: column;
  gap: 36px;
  position: relative;
}

.reg-step-card {
  position: relative;
  background: var(--grad-card);
  border: 1px solid var(--border-card);
  border-radius: 24px;
  padding: 36px 34px 40px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35);
  transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.5s ease, border-color 0.4s ease, background 0.4s ease;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  display: flex;
  flex-direction: column;
}

/* Scroll entrance state */
.reg-step-card.reveal-init {
  opacity: 0;
  transform: translateY(35px) scale(0.97);
  transition: opacity 0.7s cubic-bezier(0.16, 1, 0.3, 1), transform 0.7s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.5s ease, border-color 0.4s ease;
}

.reg-step-card.revealed {
  opacity: 1;
  transform: translateY(0) scale(1);
}

/* Luminous connecting line between step cards */
.reg-step-card:not(:last-child)::after {
  content: '';
  position: absolute;
  bottom: -36px;
  left: 50%;
  transform: translateX(-50%);
  width: 2px;
  height: 36px;
  background: linear-gradient(to bottom, rgba(214, 145, 174, 0.85) 0%, rgba(170, 107, 151, 0.25) 100%);
  box-shadow: 0 0 12px rgba(214, 145, 174, 0.6);
  z-index: 2;
}

.reg-step-card:hover {
  border-color: var(--border-card-hover);
  background: var(--grad-card-hover);
  transform: translateY(-5px);
  box-shadow: 0 24px 55px rgba(0, 0, 0, 0.45), var(--glow-accent);
}

.reg-step-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 12px;
}

.reg-step-num {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(214, 145, 174, 0.4), rgba(170, 107, 151, 0.7));
  color: var(--color-white);
  font-size: 1.2rem;
  font-weight: 800;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 18px rgba(214, 145, 174, 0.45);
  flex-shrink: 0;
  border: 1.5px solid rgba(255, 255, 255, 0.6);
  transition: transform 0.4s ease, box-shadow 0.4s ease;
}

.reg-step-card:hover .reg-step-num {
  transform: scale(1.08) rotate(5deg);
  box-shadow: 0 0 24px rgba(214, 145, 174, 0.75), var(--glow-button);
}

.reg-step-title {
  color: var(--text-title);
  font-size: clamp(1.25rem, 2.3vw, 1.55rem);
  font-weight: 800;
  line-height: 1.35;
  letter-spacing: -0.015em;
  margin: 0;
}

.reg-step-desc {
  color: var(--text-body);
  font-size: 1.05rem;
  line-height: 1.7;
  margin-bottom: 24px;
}

/* Dynamic 3D Showcase Stage for Registration Mockup Images */
.reg-step-media {
  position: relative;
  border-radius: 22px;
  overflow: hidden;
  border: 1.5px solid rgba(214, 145, 174, 0.4);
  background: radial-gradient(ellipse at 50% 25%, rgba(118, 56, 99, 0.45) 0%, rgba(45, 6, 33, 0.85) 60%, rgba(18, 2, 14, 0.95) 100%);
  box-shadow: 
    0 20px 50px rgba(0, 0, 0, 0.55),
    0 0 32px rgba(214, 145, 174, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.2);
  width: 100%;
  max-width: 100%;
  padding: 14px;
  margin: 0;
  perspective: 1100px;
  transform-style: preserve-3d;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s ease, border-color 0.5s ease;
}

/* Shimmering reflective light beam sweep */
.reg-step-media::after {
  content: '';
  position: absolute;
  top: -60%;
  left: -80%;
  width: 140%;
  height: 220%;
  background: linear-gradient(
    105deg,
    transparent 35%,
    rgba(255, 255, 255, 0.08) 46%,
    rgba(244, 225, 226, 0.24) 50%,
    rgba(255, 255, 255, 0.08) 54%,
    transparent 65%
  );
  transform: rotate(25deg);
  pointer-events: none;
  z-index: 5;
  animation: shimmerSweep 7.5s infinite ease-in-out;
}

.reg-step-media img {
  width: 100%;
  height: auto;
  object-fit: cover;
  display: block;
  border-radius: 16px;
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
  transition: transform 0.5s cubic-bezier(0.16, 1, 0.3, 1), filter 0.4s ease;
}

/* Alternating subtle dynamic tilt & float animations */
#step-1 .reg-step-media {
  animation: floatMockupA 5.6s ease-in-out infinite alternate;
  animation-delay: 0s;
}

#step-2 .reg-step-media {
  animation: floatMockupB 6.0s ease-in-out infinite alternate;
  animation-delay: 0.8s;
}

#step-3 .reg-step-media {
  animation: floatMockupA 5.2s ease-in-out infinite alternate;
  animation-delay: 1.6s;
  border-color: rgba(240, 163, 190, 0.65);
  box-shadow: 
    0 24px 60px rgba(0, 0, 0, 0.6),
    0 0 45px rgba(214, 145, 174, 0.35),
    inset 0 1px 0 rgba(255, 255, 255, 0.3);
}

#step-4 .reg-step-media {
  animation: floatMockupB 6.2s ease-in-out infinite alternate;
  animation-delay: 2.2s;
}

#step-5 .reg-step-media {
  animation: floatMockupA 5.8s ease-in-out infinite alternate;
  animation-delay: 2.8s;
}

/* Floating 3D Keyframes (Left tilt & Right tilt) */
@keyframes floatMockupA {
  0% {
    transform: perspective(1000px) rotateX(2.2deg) rotateY(-1.8deg) rotateZ(-0.5deg) translateY(0px);
  }
  100% {
    transform: perspective(1000px) rotateX(1.2deg) rotateY(-0.8deg) rotateZ(-0.2deg) translateY(-10px);
  }
}

@keyframes floatMockupB {
  0% {
    transform: perspective(1000px) rotateX(2.2deg) rotateY(1.8deg) rotateZ(0.5deg) translateY(0px);
  }
  100% {
    transform: perspective(1000px) rotateX(1.2deg) rotateY(0.8deg) rotateZ(0.2deg) translateY(-10px);
  }
}

@keyframes shimmerSweep {
  0% {
    left: -80%;
    opacity: 0;
  }
  15% {
    opacity: 1;
  }
  45% {
    left: 120%;
    opacity: 1;
  }
  50%, 100% {
    left: 120%;
    opacity: 0;
  }
}

/* Hover interaction: levels up, floats forward, and radiates */
.reg-step-card:hover .reg-step-media {
  animation-play-state: paused;
  transform: perspective(1000px) rotateX(0deg) rotateY(0deg) rotateZ(0deg) translateY(-10px) scale(1.02);
  box-shadow: 
    0 30px 70px rgba(0, 0, 0, 0.65), 
    0 0 50px rgba(214, 145, 174, 0.5),
    inset 0 1px 0 rgba(255, 255, 255, 0.4);
  border-color: rgba(244, 225, 226, 0.85);
}

.reg-step-card:hover .reg-step-media img {
  transform: scale(1.015);
  filter: brightness(1.03) contrast(1.02);
}

/* Highlighted Step 3 - Agency ID Box */
.reg-step-highlight {
  border: 1.5px solid var(--color-emerald);
  background: rgba(58, 12, 44, 0.78);
  box-shadow: 0 20px 50px rgba(170, 107, 151, 0.38);
}

.agency-id-callout {
  margin-bottom: 24px;
  background: rgba(24, 3, 18, 0.88);
  border-radius: var(--radius-md);
  padding: 24px;
  border: 1.5px solid var(--color-emerald);
  box-shadow: 0 0 25px rgba(170, 107, 151, 0.35);
}"""

css = re.sub(reg_pattern, reg_replacement, css, flags=re.DOTALL)
print("Registration section updated via regex")

# 4. Update mobile breakpoint for reg-step-media
mobile_reg = """.reg-step-media {
    max-width: 100%;
    margin-top: 0;
  }"""

mobile_replacement = """.reg-step-media {
    max-width: 100%;
    margin-top: 0;
    padding: 8px;
    border-radius: 18px;
  }

  #step-1 .reg-step-media,
  #step-2 .reg-step-media,
  #step-3 .reg-step-media,
  #step-4 .reg-step-media,
  #step-5 .reg-step-media {
    transform: none !important;
    animation: floatMockupMobile 4.5s ease-in-out infinite alternate !important;
  }

  .reg-step-card:hover .reg-step-media {
    transform: translateY(-4px) !important;
  }

@keyframes floatMockupMobile {
  0% { transform: translateY(0px); }
  100% { transform: translateY(-6px); }
}"""

if mobile_reg in css:
    css = css.replace(mobile_reg, mobile_replacement)
    print("Mobile reg updated successfully")
else:
    print("Mobile reg target not found directly, checking regex")
    css = re.sub(r'\.reg-step-media\s*\{\s*max-width:\s*100%;\s*margin-top:\s*0;\s*\}', mobile_replacement, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Saved style.css successfully")

