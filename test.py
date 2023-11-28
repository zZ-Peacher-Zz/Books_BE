import requests

BASE = 'http://127.0.0.1:5000'
headers = {'Content-Type': 'application/json'}

response = requests.post(BASE + "/users/1007", {"name":"Helloworld"}, headers=headers)

print(response.json())