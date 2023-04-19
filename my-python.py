import json
import requests
import random

url = "http://localhost:8069/jsonrpc"

db = "NewBD"
user = "HuyLT"
api_key = "7fb4b71eb780cb0ec59d550ea015dd17110f1b0f"

data = {
    'jsonrpc': '2.0',
    'method': 'call',   
    'params': {
        'service': 'object',
        'method': 'execute_kw',
        'args': (db, 2, api_key, "tutorial.library.book", "search", [[["name", "ilike", "rpc"]]])
    },
    'id': random.randint(0, 1000000000)
}

res = requests.post(url, json=data, headers={"Content-Type": "application/json"})
# res_content_str = res.content.decode('utf-8') 
# res_json = json.loads(res_content_str) 

res_json = json.loads(res.content.decode('utf-8')) 

if res_json:
    print("Kết nối với server Odoo thành công!")
    print(res_json)
else:
    print("Không thể kết nối với server Odoo.")

print(res_json)
print(data)
