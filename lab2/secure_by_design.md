# Challenge `Secure by Design` writeup

- Vulnerability: Cookie poisoning
- Where: In the `user` cookie
- Impact: Get access to the admin's account

## Finding the vulnerability / Steps to reproduce

1. Using a regular nickname returns no unusual behaviour. However, using `admin` as a nickname returns a message for non-admins with the `fake-admin` display name.
2. Accessing the cookies shows us that `user` contains a base 64 encoding of the display name (`fake-admin` if the chosen nickname was `admin`, the nickname otherwise).
3. Making a request with a tampered cookie containing a base 64 encoding of `admin` in the `user` field bypasses the form sanitisation step and gives us admin privileges (and the flag: `SSof{Base64_encoding_is_not_a_protection}`).

[(POC)](`secure_by_design.py`)
