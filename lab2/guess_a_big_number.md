# Challenge `Guess a BIG number` writeup

- Vulnerability: Brute-force attack
- Where: In the `/number` endpoint
- Impact: It allows to find the server's guess by enumeration

## Finding the vulnerability / Steps to reproduce

1. Since the game gives the player hints as to whether the server's number is higher or lower, it's possible to get it via a brute-force attack using binary search.
2. We start by keeping a `lower_bound` at `0` and an `upper_bound` at `100000` and make a `guess` using the average of both values.
  - If the server returns `Higher!`, the `lower_bound` is set to `guess + 1`.
  - If it returns `Lower`, the `upper_bound` is set to `guess - 1`.
  - Otherwise, the flag (`SSof{A_little_scripting_is_all_you_need}`) is returned.

Note: The number is associated with the player's cookie, so a session must be kept in order to keep on guessing.

[(POC)](`guess_a_big_number.py`)