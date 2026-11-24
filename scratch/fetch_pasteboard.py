import urllib.request
import re

url = 'https://pasteboard.co/IytyiyjE8e25.png'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        content_type = resp.headers.get('Content-Type')
        print('Content-Type:', content_type)
        data = resp.read()
        print('Data length:', len(data))
        if content_type and 'image' in content_type:
            with open('pasteboard_img.png', 'wb') as f:
                f.write(data)
            print('Saved pasteboard_img.png directly')
        else:
            text = data.decode('utf-8', errors='ignore')
            with open('pasteboard.html', 'w', encoding='utf-8') as f:
                f.write(text)
            # Find meta og:image or similar
            og_img = re.search(r'<meta property="og:image" content="([^"]+)"', text)
            if og_img:
                img_url = og_img.group(1)
                print('Found og:image:', img_url)
                req2 = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(req2) as resp2:
                    with open('pasteboard_img.png', 'wb') as f2:
                        f2.write(resp2.read())
                print('Saved pasteboard_img.png from og:image')
            else:
                print('No og:image found')
except Exception as e:
    print('Error:', e)

