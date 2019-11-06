import requests
import json

with requests.get("http://localhost:5000/data", stream=True) as r:
    # print(r)
    # q = r.content
    # print(q)

    for res in r.iter_lines():
        print(json.loads(res))