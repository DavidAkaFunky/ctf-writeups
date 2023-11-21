# Challenge `Pwntools Requests` writeup

- Vulnerability: Brute-force attack
- Where: By sending the `MORE` string
- Impact: Get the target number via multiple requests

## Finding the vulnerability / Steps to reproduce

1. As the game says, the player must keep on making requests by sending the `MORE` string until the current number matches the target number:
  - If the number is below the target, the server will add a positive number to it.
  - If the number exceeds the target at some stage, the server will add a negative number to it.
  - In both numbers match, the player must enter the `FINISH` string, and the flag (`SSof{You_can_also_script_over_sockets}`) will be given. 
2. This game can be brute-forced using the script in the link below to read the content of the server line by line and respond accordingly until both numbers match and the challenge is solved.

[(POC)](`pwntools_sockets.py`)