import requests

url = "http://10.20.197.205:1880/int-json"

datax = {"name":"Ananda Miarta", "nim":1301174166, "message":"Hay Sayang"}

r = requests.post(url, json=datax)

print r

print r.text