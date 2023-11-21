# Challenge `Python Requests` writeup

- Vulnerability: Brute-force attack
- Where: In the `/more` endpoint + No rate limit enforcement
- Impact: Get the target number via multiple requests

## Finding the vulnerability / Steps to reproduce

1. As the game says, the player must keep on making requests to the `/more` endpoint until the current number matches the target number:
  - If the number is below the target, the server will add a positive number to it.
  - If the number exceeds the target at some stage, the server will add a negative number to it.
  - In both numbers match, the player must make a request to the `/finish` endpoint, and the flag (`SSof{Learning_python_requests_is_a_good_complement_to_ZAP}`) will be given. 
2. This game can be brute-forced using the script in the link below to automatically make requests until both numbers match and the challenge is solved.

[(POC)](`python_requests.py`)
