import requests
import re

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

# Get options.php
r = s.get('https://boloupgo.live/wp-admin/options.php', verify=False)
print('options.php status:', r.status_code)

# Find all hidden inputs in options.php
hidden_inputs = dict(re.findall(r'<input\s+type="hidden"\s+name="([^"]+)"\s+value="([^"]*)"', r.text))
print('Hidden inputs:', list(hidden_inputs.keys()))

# In options.php, any option can be updated by posting its name and value, plus the hidden fields!
# Let's inspect what hidden fields options.php has:
# Usually: _wpnonce, _wp_http_referer, action (often 'update')
nonce_match = re.search(r'name="_wpnonce"\s+value="([^"]+)"', r.text)
nonce = nonce_match.group(1) if nonce_match else None
print('Nonce:', nonce)

# Also find site_icon input
site_icon_match = re.search(r'name="site_icon"[^>]*value="([^"]*)"', r.text)
print('Current site_icon value:', site_icon_match.group(1) if site_icon_match else 'Not found')

# Let's prepare post data with all fields or just the ones needed
# When submitting options.php, WordPress parses all inputs in the form.
# Let's see: we can parse ALL inputs in options.php form!
all_inputs = dict(re.findall(r'<input[^>]+name="([^"]+)"[^>]+value="([^"]*)"', r.text))
print(f'Total inputs found: {len(all_inputs)}')
all_inputs['site_icon'] = '65' # Our newly uploaded boloup-favicon media ID

# Post to options.php
r_post = s.post('https://boloupgo.live/wp-admin/options.php', data=all_inputs, verify=False, allow_redirects=True)
print('Post status:', r_post.status_code)
print('Post url:', r_post.url)

# Check if site_icon updated
r_check = s.get('https://boloupgo.live/wp-admin/options.php', verify=False)
site_icon_check = re.search(r'name="site_icon"[^>]*value="([^"]*)"', r_check.text)
print('New site_icon value:', site_icon_check.group(1) if site_icon_check else 'Not found')

