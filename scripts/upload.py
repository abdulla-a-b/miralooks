import requests
import json
import os
WC_URL = "https://miralooks.com/wp-json/wc/v3/helloproducts"
CK = "ck_8971f5fb93a23b4d8f2e079f0a7a002c720c7c97"
CS = "cs_6de72383d046244c94c3075e736aac6f3353fd48"

folder = "helloproducts"

for file in os.listdir(folder):
  if file.endwith(".json"):
    
     with open(os.path.join(folder, file) as f:
       data = json.load(f)

     r = requests.post(
       WC_URL,
       auth=(CK, CS),
       jason=data,
       timeout=30
     )

     print(r.text)

