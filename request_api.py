import requests

input=input('Inputkan ID untuk request API\n')

resp = requests.get('http://seskiramadhan.pythonanywhere.com/api?id='+input)
data = resp.json()
data = data[0]
data = data["katakata"]
print(data)
