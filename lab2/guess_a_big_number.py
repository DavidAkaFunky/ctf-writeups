import requests

SERVER='http://mustard.stt.rnl.tecnico.ulisboa.pt:22052'

r = requests.get(SERVER)
cookies = r.cookies

lower_bound = 0
upper_bound = 100000

while True:
    guess = (lower_bound + upper_bound) // 2
    r = requests.get(SERVER + "/number/{}".format(guess), cookies=cookies)
    text = r.text
    if "Lower" in text:
        upper_bound = guess - 1
    elif "Higher" in text:
        lower_bound = guess + 1
    else:
        print(text)
        break