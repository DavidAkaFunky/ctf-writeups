# Challenge `Python Requests Again` writeup

- Vulnerability: Brute-force attack + Cookie poisoning
- Where: In the `/more` endpoint + the `remaining_tries` cookie + No rate limit enforcement
- Impact: Get the target number via multiple requests and cookie poisoning

## Finding the vulnerability / Steps to reproduce

1. As the game says, the player has one attempt to get the target number (and the flag, `SSof{Client_side_validation_is_a_big_NO}`), otherwise they're forced to start again.
2. However, this attempt limit is only enforced by a cookie value called `remaining_tries`, which is decremented with each attempt and is used to force the player to restart if the value is `0`. This conclusion was achieved by doing two things which let an attacker get infinite attempts:
  - Repeatedly tampering the cookie with a positive number;
  - Tampering only once with a negative number.
3. As such, this game can also be brute-forced using a script (see the link below) to do one of the two aforementioned techniques, and repeat the game until it's solved. Although both techniques were tested, the final script contains the second one.

[(POC)](`python_requests_again.py`)