import json
import re

with open('preview.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<body[^>]*>(.*)</body>', html, re.DOTALL | re.IGNORECASE)
body_content = match.group(1).strip() if match else html.strip()

body_json = json.dumps(body_content)

js_content = f"""async (page) => {{
  const htmlContent = {body_json};

  const res = await page.evaluate(async (newHtml) => {{
    const e = window['$e'];
    const currentDoc = elementor.documents.getCurrent();

    // 1. Set template to elementor_canvas
    try {{
      await e.run('document/elements/settings', {{
        container: currentDoc.container,
        settings: {{ template: 'elementor_canvas' }}
      }});
    }} catch (err) {{
      console.warn('Set template via $e failed, setting on model directly:', err);
      elementor.settings.page.model.set('template', 'elementor_canvas');
    }}

    // 2. Find HTML widget
    const allContainers = currentDoc.container.children;
    let targetContainer = null;

    function findWidget(container) {{
      if (container.model && container.model.get('widgetType') === 'html') {{
        return container;
      }}
      if (container.children) {{
        for (const child of container.children) {{
          const found = findWidget(child);
          if (found) return found;
        }}
      }}
      return null;
    }}

    for (const child of allContainers) {{
      targetContainer = findWidget(child);
      if (targetContainer) break;
    }}

    if (!targetContainer) {{
      return {{ success: false, error: 'HTML widget container not found' }};
    }}

    // 3. Update HTML widget content
    await e.run('document/elements/settings', {{
      container: targetContainer,
      settings: {{ html: newHtml }}
    }});

    // 4. Save and Publish document
    await e.run('document/save/publish');

    return {{
      success: true,
      widgetId: targetContainer.id,
      template: elementor.settings && elementor.settings.page && elementor.settings.page.model ? elementor.settings.page.model.get('template') : null
    }};
  }}, htmlContent);

  return res;
}}
"""

with open('scratch/sync_elementor_page.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Generated scratch/sync_elementor_page.js successfully")

