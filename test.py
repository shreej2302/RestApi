import requests as r

BASE = "http://127.0.0.1:5000/"

response = r.get(BASE + "video/2")
print(response.json())
#print(response)