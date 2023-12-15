# Challenge `I will take care of this site` writeup

- Vulnerability: SQL injection
- Where: In the login form fields
- Impact: It allows to login as the admin

## Finding the vulnerability / Steps to reproduce

1. The first thing that was tried in all described vulnerabilites was a string that closed one of the input fields in the SQL query and also created an error - for example, `'aaa`, as the query's template with the input string would then be displayed as part of the error.

2. In this challenge, the vulnerable query was `SELECT id, username, password, bio, age, jackpot_val FROM user WHERE username = '{%s}' AND password = 'hash({%s})'`, where `{%s}` are input fields.

3. This means the query can be exploited, for example, using `admin' -- `, which sets the `username` to `admin` and escapes the remaining query string as comment, thus requiring no password.

4. When entering the admin's profile page, the flag (`SSof{SQLi_on_SELECT_allows_you_to_become_an_admin}`) can then be found.