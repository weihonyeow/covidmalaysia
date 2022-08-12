import requests
import json
url='http://127.0.0.1:5000/'
req = requests.get(url)
print(req.text)