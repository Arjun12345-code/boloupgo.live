tilt_script = """      // Scroll Reveal Animation for Registration Step Cards & Media Showcase
      if ('IntersectionObserver' in window) {
        var revealObserver = new IntersectionObserver(function (entries, observer) {
          entries.forEach(function (entry) {
            if (entry.isIntersecting) {
              entry.target.classList.add('revealed');
              observer.unobserve(entry.target);
            }
          });
        }, {
          threshold: 0.12,
          rootMargin: '0px 0px -40px 0px'
        });

        document.querySelectorAll('.reg-step-card').forEach(function (card) {
          card.classList.add('reveal-init');
          revealObserver.observe(card);
        });
      }

      // Dynamic 3D Interactive Tilt on Hover for Registration Mockups (Desktop)
      if (window.matchMedia('(min-width: 992px)').matches) {
        document.querySelectorAll('.reg-step-card').forEach(function (card) {
          var media = card.querySelector('.reg-step-media');
          if (!media) return;

          card.addEventListener('mousemove', function (e) {
            var rect = card.getBoundingClientRect();
            var x = e.clientX - rect.left;
            var y = e.clientY - rect.top;
            var centerX = rect.width / 2;
            var centerY = rect.height / 2;
            var tiltX = ((y - centerY) / centerY) * -4;
            var tiltY = ((x - centerX) / centerX) * 4;

            media.style.transform = 'perspective(1000px) rotateX(' + tiltX.toFixed(2) + 'deg) rotateY(' + tiltY.toFixed(2) + 'deg) translateY(-8px) scale(1.02)';
          });

          card.addEventListener('mouseleave', function () {
            media.style.transform = '';
          });
        });
      }
"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Don't add if already added
    if 'Dynamic 3D Interactive Tilt' in content:
        print(f"Already updated {filepath}")
        return

    target = "    })();\n  </script>"
    if target in content:
        content = content.replace(target, tilt_script + "    })();\n  </script>")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath} successfully")
    else:
        print(f"Target not found in {filepath}")

update_file('index.html')
update_file('preview.html')

