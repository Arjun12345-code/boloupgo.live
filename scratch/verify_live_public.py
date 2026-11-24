import requests, urllib3, re
urllib3.disable_warnings()

r = requests.get('https://boloupgo.live/', verify=False)
hero_match = re.search(r'<div class="hero-actions"[^>]*>(.*?)</div>', r.text, re.DOTALL)
if hero_match:
    print('Hero Actions Content:\n', hero_match.group(1).strip())
cta_match = re.search(r'<div class="cta-actions"[^>]*>(.*?)</div>', r.text, re.DOTALL)
if cta_match:
    print('Final CTA Actions Content:\n', cta_match.group(1).strip())
