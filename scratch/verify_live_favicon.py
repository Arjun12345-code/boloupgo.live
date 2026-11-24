import requests
import time

url = f'https://boloupgo.live/?t={int(time.time())}'
r = requests.get(url, verify=False)
print('Status:', r.status_code)
for line in r.text.splitlines():
    lower = line.lower()
    if 'rel="icon"' in lower or 'rel="apple-touch-icon"' in lower or 'msapplication-tileimage' in lower:
        print('FOUND:', line.strip())

