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

r_admin = s.get('https://boloupgo.live/wp-admin/', verify=False)
match = re.search(r'href="([^"]*litespeed-purge=all[^"]*)"', r_admin.text)
if match:
    purge_url = match.group(1).replace('&amp;', '&')
    print('Purge URL:', purge_url)
    r_purge = s.get(purge_url, verify=False)
    print('Purge response status:', r_purge.status_code)
else:
    print('Searching admin bar for purge...')
    matches = [m for m in re.findall(r'href="([^"]+)"', r_admin.text) if 'purge' in m.lower()]
    print('Found:', matches)
    for m in matches:
        s.get(m.replace('&amp;', '&'), verify=False)
        print('Triggered:', m)

