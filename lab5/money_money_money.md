# Challenge `Money, money, money` writeup

- Vulnerability: SQL injection
- Where: In the profile page's bio field
- Impact: It allows to update the number of tokens required for the jackpot

## Finding the vulnerability / Steps to reproduce

1. After sending a string which throws an SQL error, the vulnerable query was then displayed: `UPDATE user SET bio = '{%s}' WHERE username = '{USER}'`, where `{%s}` is an input field and `{USER}` is the username used to create the account to be exploited.

2. This means the query can be exploited, for example, using `', jackpot_val = 0, bio='`, which sets the number of tokens required for the jackpot (`jackpot_val`) to 0, which matches the current amount collected. Unlike the first challenge, no comments can be used to escape the remaining query string.

3. As a result, the jackpot, containing the flag (`SSof{How_did_you_UPDATE_your_tokens}`), can then be found.