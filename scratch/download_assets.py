import urllib.request
import os

items = [
  {'id': '1_V40shKvFWLaP_Ixce6-PIj_ntCIox0Z', 'name': 'BoloUp Ecosystem.png'},
  {'id': '1xutz7Rw-lytGgUxM7nnUo-4onTkR2Jq6', 'name': 'BoloUp Host Role.png'},
  {'id': '1bFpfkQElaVrgzxP9LLZO738tuyL4ymOA', 'name': 'BoloUp Agent Role.png'},
  {'id': '1OJ5eoIhPnsP8SqpEurmS3k-uvG6yQkNj', 'name': 'BoloUp Add New Host.png'},
  {'id': '1ZDzUrk9NHce46N9b-LYcHYc68PSPupn7', 'name': 'BoloUp - Host Registration Guide Step 1.jpg'},
  {'id': '1Orv6WjpMy9wdvPevGQXIQy0D7eeBTzAG', 'name': 'BoloUp - Host Registration Guide Step 2.jpg'},
  {'id': '1gaeOv6HaJ7Exhxpog2twi1_6b0KJ3Dfm', 'name': 'BoloUp - Host Registration Guide Step 3.jpg'},
  {'id': '1UbXCgRt_Dvp7LaxCAtqp1m0445iBST9T', 'name': 'BoloUp - Host Registration Guide Step 4.jpg'},
  {'id': '1217Gu1E6jfvJATrl1cyaMk2dxzDR-smi', 'name': 'BoloUp - AgentHost Withdraw.jpg'},
  {'id': '1iQKohOVmZtwr2X61MpW5w32vB3eBSpEX', 'name': 'BoloUp - Agency Registration - Step 1.png'},
  {'id': '1q3d-RNZ-xgEtIhGPZNR2O6EinVpzTJop', 'name': 'BoloUp - Agency Registration - Step 2.png'},
  {'id': '1W437EBqQUXbAbi-aIsUFPVjcLkF_b7FP', 'name': 'BoloUp - Agency Registration - Step 3.png'},
  {'id': '1eJBI5R9yaSf8Msgugm-ncGoRD58lnPXm', 'name': 'BoloUp - Agency Registration - Step 4.jpg'},
  {'id': '1PmBkpQbX2r9dFjCNW16Ro5aPpn8tZfsJ', 'name': 'BoloUp - Agent Add New Host Part 1.jpg'},
  {'id': '1Yy3KOpc5P98A0vSSwY2YZWEZT4QxIUbg', 'name': 'BoloUp - Agent Add New Host Part 2.jpg'},
]

os.makedirs('temp_drive_assets', exist_ok=True)
for item in items:
    path = os.path.join('temp_drive_assets', item['name'])
    if not os.path.exists(path):
        print(f"Downloading {item['name']}...")
        url = f"https://drive.google.com/uc?export=download&id={item['id']}"
        urllib.request.urlretrieve(url, path)
        print(f"Saved {item['name']}: {os.path.getsize(path)} bytes")
    else:
        print(f"Already exists: {item['name']}: {os.path.getsize(path)} bytes")

