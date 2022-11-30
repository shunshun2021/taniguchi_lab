import requests
import json

url = "http://127.0.0.1:8000/all"

r = requests.get(url)

data = r.json()

for v in data.values():
    for i in range(len(v)):
        # v[i] : i番目のタプル
        print(v[i])
