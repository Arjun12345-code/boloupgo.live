import re

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # Remove <div class="reg-step-content">
    text = re.sub(r'[ \t]*<div class="reg-step-content">\r?\n', '', text)

    # Remove the matching closing </div> right before <div class="reg-step-media">
    text = re.sub(r'(</p>\r?\n)[ \t]*</div>(\r?\n[ \t]*<div class="reg-step-media">)', r'\1\2', text)
    text = re.sub(r'(</div>\r?\n[ \t]*</div>\r?\n)[ \t]*</div>(\r?\n[ \t]*<div class="reg-step-media">)', r'\1\2', text)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Done cleaning {filepath}')

clean_file('index.html')
clean_file('preview.html')

