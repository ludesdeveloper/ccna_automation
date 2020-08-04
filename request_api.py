import requests

resp = requests.get('http://seskiramadhan.pythonanywhere.com/api?id=8')
data = resp.json()
data = data[0]
data = data["katakata"]
print(data)