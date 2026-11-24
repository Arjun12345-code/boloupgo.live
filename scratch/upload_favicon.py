import requests
import re
import os

login_url = 'https://boloupgo.live/1c86y6aypsqcbgpgxvhw0-fow_zml13r66c_jfigjdfk'
s = requests.Session()
data = {
    'log': 'webdev',
    'pwd': '4fATejbE7aqEleKEaIwQa6@l',
    'wp-submit': 'Log In',
    'redirect_to': 'https://boloupgo.live/wp-admin/',
    'testcookie': '1'
}
s.post(login_url, data=data, verify=False, allow_redirects=True)

# 1. Check media-new.php
r = s.get('https://boloupgo.live/wp-admin/media-new.php', verify=False)
print('media-new status:', r.status_code)

# Find wp_nonce
match = re.search(r'name="_wpnonce"\s+value="([a-f0-9]+)"', r.text)
if not match:
    match = re.search(r'_wpnonce["\':\s]+([a-f0-9]{10})', r.text)
nonce = match.group(1) if match else None
print('Found nonce:', nonce)

# 2. Upload using async-upload.php
file_path = 'assets/images/boloup-favicon-512x512.png'
with open(file_path, 'rb') as f:
    files = {'async-upload': ('boloup-favicon.png', f, 'image/png')}
    upload_data = {
        'name': 'boloup-favicon.png',
        'action': 'upload-attachment',
        '_wpnonce': nonce,
    }
    r_up = s.post('https://boloupgo.live/wp-admin/async-upload.php', data=upload_data, files=files, verify=False)
    print('Upload status:', r_up.status_code)
    print('Upload response:', r_up.text[:300])

