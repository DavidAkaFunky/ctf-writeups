# Challenge `Another jackpot` writeup

- Vulnerability: Race condition (lack of atomicity)
- Where: In the `login` function, with an effect on the `jackpot` function
- Impact: It allows to run the `jackpot` function as admin

## Finding the vulnerability / Steps to reproduce

1. In the `login` function, we can see the `current_session`'s `username` parameter to be replaced with the login form's `username` field, thus tainting its integrity. This means that, even if we input incorrect credentials, that value won't be sanitised until the `username` is set to `None`, leaving a timeframe where an arbitrary `username` is associated to that session entity in the database.
2. This means an attacker can create a script (like the one below) which runs two loops in parallel: one that repeatedly attemps to login using the `admin` username, and another that attempts to enter the jackpot with the current session; eventually, there will be an instance when the `get_current_section` call in the `jackpoint` function returns during the aforementioned timeframe, meaning the returned message is the flag: `SSof{There_was_never_an_admin}`.

[(POC)](`jackpot.py`)