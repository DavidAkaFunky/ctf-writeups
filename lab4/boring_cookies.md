# Challenge `Just my boring cookies` writeup

- Vulnerability: XSS
- Where: In the search form field
- Impact: It allows the retrieval of the session's cookies

## Finding the vulnerability / Steps to reproduce

1. An immediate test for XSS proneness is a simple `<script>alert(1)</script`. Since the browser effectly shows an alert, it can be attacked using XSS.
2. An attacker just needs to send `<script>alert(document.cookie)</script` to retrieve the flag (`SSof{YOU_HAVE_NO_SECRETS}`).