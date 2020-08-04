import requests

resp = requests.get('http://127.0.0.1:5000/api?id=4')
data = resp.json()
data = data[0]
data = data["katakata"]
print(data)