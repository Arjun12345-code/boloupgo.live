import json

with open('style.css', 'r', encoding='utf-8') as f:
    css_content = f.read()

payload = f"<style>\n{css_content}\n</style>"

# Write to a js file that can be evaluated in playwright
with open('scratch/post25_payload.json', 'w', encoding='utf-8') as f:
    json.dump({'code': payload}, f)

print(f"Payload created, length: {len(payload)}")

