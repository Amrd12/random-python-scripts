import requests
url = "http://192.168.1.1/"
token = {
    "action" :"login",
    "Username" : "admin",
    "Password" : "amr12alnbawy"
}
headers = { "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42"}
s = requests.session()
s.post("http://192.168.1.1/start.ghtml",data=token , headers=headers)
req = s.get(url ="http://192.168.1.1/start.ghtml",headers = headers)
print(req.text,req.status_code)
