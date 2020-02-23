import requests

url = "http://localhost:1880/int-json"

datax = {"name":"Ananda Miarta", "nim":1301174166, "message":"Hay Sayang"}

r = requests.get(url, json=datax)

print r

print r.text
