import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update .registration-timeline-wrap
css = re.sub(
    r'\.registration-timeline-wrap\s*\{[^}]*\}',
    '''.registration-timeline-wrap {
  max-width: 780px;
  margin: 0 auto;
  position: relative;
}''',
    css
)

# Update .reg-step-media to max-width: 580px; margin: 0 auto; cursor: zoom-in;
old_media = """.reg-step-media {
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
}"""

new_media = """.reg-step-media {
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
  max-width: 580px;
  padding: 12px;
  margin: 0 auto;
  perspective: 1100px;
  transform-style: preserve-3d;
  transition: transform 0.6s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.6s ease, border-color 0.5s ease;
  cursor: zoom-in;
}

/* Floating zoom icon hint on hover */
.reg-step-media::before {
  content: '';
  position: absolute;
  top: 18px;
  right: 18px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(35, 5, 26, 0.85) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='18' height='18' viewBox='0 0 24 24' fill='none' stroke='%23f4e1e2' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Ccircle cx='11' cy='11' r='8'%3E%3C/circle%3E%3Cline x1='21' y1='21' x2='16.65' y2='16.65'%3E%3C/line%3E%3Cline x1='11' y1='8' x2='11' y2='14'%3E%3C/line%3E%3Cline x1='8' y1='11' x2='14' y2='11'%3E%3C/line%3E%3C/svg%3E") no-repeat center;
  border: 1px solid rgba(214, 145, 174, 0.6);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), 0 0 12px rgba(214, 145, 174, 0.3);
  opacity: 0;
  transform: scale(0.8);
  transition: opacity 0.3s ease, transform 0.3s ease;
  z-index: 6;
  pointer-events: none;
}

.reg-step-card:hover .reg-step-media::before {
  opacity: 1;
  transform: scale(1);
}"""

if old_media in css:
    css = css.replace(old_media, new_media)
    print("Replaced old_media in style.css")
else:
    print("old_media not found directly, using regex")
    css = re.sub(
        r'\.reg-step-media\s*\{[^}]*width:\s*100%;\s*max-width:\s*100%;[^}]*\}',
        new_media,
        css
    )

# Update .agency-id-callout
css = re.sub(
    r'\.agency-id-callout\s*\{[^}]*\}',
    '''.agency-id-callout {
  margin: 0 auto 24px;
  max-width: 580px;
  background: rgba(24, 3, 18, 0.88);
  border-radius: var(--radius-md);
  padding: 24px;
  border: 1.5px solid var(--color-emerald);
  box-shadow: 0 0 25px rgba(170, 107, 151, 0.35);
}''',
    css
)

# Update .about-img-wrap to have cursor: zoom-in
css = re.sub(
    r'\.about-img-wrap\s*\{([^}]*)\}',
    r'.about-img-wrap {\1  cursor: zoom-in;\n}',
    css
)

# Append Lightbox modal CSS if not present
lightbox_css = """
/* ==========================================================================
   18. Image Lightbox Modal Component
   ========================================================================== */
.lightbox-modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 99999;
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1), visibility 0.3s ease;
  padding: 20px;
}

.lightbox-modal.active {
  opacity: 1;
  visibility: visible;
}

.lightbox-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(16, 2, 13, 0.92);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  cursor: pointer;
}

.lightbox-content {
  position: relative;
  z-index: 2;
  max-width: 900px;
  max-height: 90vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  transform: scale(0.92) translateY(20px);
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.lightbox-modal.active .lightbox-content {
  transform: scale(1) translateY(0);
}

.lightbox-close {
  position: absolute;
  top: -48px;
  right: 0;
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: rgba(214, 145, 174, 0.25);
  border: 1.5px solid rgba(214, 145, 174, 0.5);
  color: var(--color-white);
  font-size: 1.6rem;
  line-height: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: var(--transition);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
}

.lightbox-close:hover {
  background: var(--grad-primary);
  transform: rotate(90deg) scale(1.1);
  box-shadow: var(--glow-button);
}

.lightbox-image-wrap {
  border-radius: 20px;
  overflow: hidden;
  border: 1.5px solid rgba(214, 145, 174, 0.45);
  box-shadow: 0 25px 70px rgba(0, 0, 0, 0.65), 0 0 45px rgba(214, 145, 174, 0.35);
  background: rgba(24, 3, 18, 0.95);
  max-height: 80vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.lightbox-img {
  max-width: 100%;
  max-height: 80vh;
  width: auto;
  height: auto;
  object-fit: contain;
  display: block;
}

.lightbox-caption {
  margin-top: 14px;
  color: var(--text-body);
  font-size: 1rem;
  font-weight: 600;
  text-align: center;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.6);
}
"""

if 'Image Lightbox Modal Component' not in css:
    css += lightbox_css
    print("Added Lightbox CSS to style.css")

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Saved style.css successfully")

# 2. Update index.html and preview.html with Lightbox HTML and JS
lightbox_html = """  <!-- Image Lightbox Modal Component -->
  <div class="lightbox-modal" id="lightbox-modal" aria-hidden="true" role="dialog" aria-modal="true" aria-label="Image Preview">
    <div class="lightbox-backdrop" id="lightbox-backdrop"></div>
    <div class="lightbox-content">
      <button type="button" class="lightbox-close" id="lightbox-close" aria-label="Close image preview">&times;</button>
      <div class="lightbox-image-wrap">
        <img src="" alt="" class="lightbox-img" id="lightbox-img">
      </div>
      <div class="lightbox-caption" id="lightbox-caption"></div>
    </div>
  </div>
"""

lightbox_js = """
      // Lightbox Modal Functionality
      var lightbox = document.getElementById('lightbox-modal');
      var lightboxImg = document.getElementById('lightbox-img');
      var lightboxCaption = document.getElementById('lightbox-caption');
      var lightboxClose = document.getElementById('lightbox-close');
      var lightboxBackdrop = document.getElementById('lightbox-backdrop');

      function openLightbox(src, alt) {
        if (!lightbox || !lightboxImg) return;
        lightboxImg.src = src;
        lightboxImg.alt = alt || '';
        if (lightboxCaption) {
          lightboxCaption.textContent = alt || '';
        }
        lightbox.classList.add('active');
        lightbox.setAttribute('aria-hidden', 'false');
        document.body.style.overflow = 'hidden';
      }

      function closeLightbox() {
        if (!lightbox) return;
        lightbox.classList.remove('active');
        lightbox.setAttribute('aria-hidden', 'true');
        document.body.style.overflow = '';
        if (lightboxImg) lightboxImg.src = '';
      }

      if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
      if (lightboxBackdrop) lightboxBackdrop.addEventListener('click', closeLightbox);

      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && lightbox && lightbox.classList.contains('active')) {
          closeLightbox();
        }
      });

      // Attach click handlers to registration media images and ecosystem images
      document.querySelectorAll('.reg-step-media, .about-img-wrap').forEach(function (frame) {
        frame.addEventListener('click', function () {
          var img = frame.querySelector('img');
          if (img) {
            openLightbox(img.currentSrc || img.src, img.alt);
          }
        });
      });
"""

def update_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Add HTML modal before <script> if not present
    if 'id="lightbox-modal"' not in html:
        footer_end = '</footer>'
        if footer_end in html:
            html = html.replace(footer_end, footer_end + '\n\n' + lightbox_html)
            print(f"Added lightbox HTML to {filepath}")

    # Add JS before })(); in <script>
    if 'openLightbox' not in html:
        target_js = '    })();\n  </script>'
        if target_js in html:
            html = html.replace(target_js, lightbox_js + target_js)
            print(f"Added lightbox JS to {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved {filepath}")

update_html('index.html')
update_html('preview.html')

