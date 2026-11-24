with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

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

target = '  <!-- Internal JavaScript'
if target in html and 'id="lightbox-modal"' not in html:
    html = html.replace(target, lightbox_html + target)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Inserted lightbox into index.html successfully')
else:
    print('Already present or target not found')

