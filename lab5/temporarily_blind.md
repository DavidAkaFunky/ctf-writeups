# Challenge `Wow, it can't be more juicy than this!` writeup

- Vulnerability: (Blind) SQL injection
- Where: In the post search field
- Impact: It allows to fetch content from other tables

## Finding the vulnerability / Steps to reproduce

1. After sending a string which throws an SQL error, the vulnerable query was then displayed: `SELECT id, title, content FROM blog_post WHERE title LIKE '%{%s}%' OR content LIKE '%{%s}%'`, where `{%s}` are input fields.

2. As the posts are not shown anymore, our best way to fetch the secret is by first finding the name of the table where it's located, then the column within it. This can be done by starting with an empty string (our `TEST_STRING`) for each of the values we want to find, then testing every character in a set of acceptable characters (alphanumeric, underscores, slashes, brackets, etc.) to see if adding that character to `TEST_STRING` returns a particular output (in our situation, 5 instead of 4 posts) and stopping once that no longer happens.

3. To get the table name, the payload template that was used was `' UNION SELECT 1, '', '' FROM sqlite_master WHERE type='table' and tbl_name NOT like 'sqlite_%' AND tbl_name != 'blog_post' AND tbl_name != 'user' AND SUBSTR(tbl_name, 1, {LEN(TEST_STRING)}) == '{TEST_STRING}' -- `. Note the exclusion of the `blog_post` and `user` tables, so that those tables couldn't return false positives for our search. This returns `super_s_sof_secrets`.

4. For the columns, the following payload template was used: `' UNION SELECT 1, '', '' FROM PRAGMA_TABLE_INFO('super_s_sof_secrets') WHERE {EXCLUDED_COLUMNS}SUBSTR(name, 1, 'super_s_sof_secrets') = '{TEST_STRING}' -- `, where `EXCLUDED_COLUMNS` adds `AND name != '{COLUMN}'` for all previously visited columns, returning two columns: `id` and `secret`.

5. Finally, to get the flag, for each of the fetched column names, the following payload template was used: `' UNION SELECT 1, '', '' FROM {COLUMN} WHERE SUBSTR({COLUMN}, 1, {LEN(TEST_STRING)}) == '{TEST_STRING}' -- `. If, when the loop is finished, `TEST_STRING` contains a substring starting with `SSof{` and ending with `}`, then that substring (the flag) is returned. This happened for the column `secret`, returning `SSof{I_am_just_partially_blind_since_I_can_gEt_yoUr_datA_using_Boolean_Injection}` as the flag.

[(POC)](`temporarily_blind.py`)