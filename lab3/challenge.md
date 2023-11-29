# Challenge `I challenge you for a race` writeup

- Vulnerability: Race condition (lack of atomicity)
- Where: Between `read_file.c`'s `access` and `fopen`'s function calls
- Impact: It allows to open the `flag` file by using a link that swaps its target between a dummy file and the `flag` file between the aformentioned calls

## Finding the vulnerability / Steps to reproduce

1. By looking at the `challenges` folder, we can find a `flag` file which is read-protected to regular users, but not to `root` users.
2. Additionally, inspecting the `read_file.c` shows us a clear lack of atomicity between `access` and `fopen`'s function calls, which is prone to a race condition.
3. This means an attacker can create a script (like the one below) which runs a loop that, in parallel, creates a symbolic link that swaps between a dummy file (with read access to regular users) and the `flag` file and runs the `challenge` file (`read_file.c`'s executable) with that link's path; eventually, there will be an instance when the `access` function call reads the dummy file, thus entering the `if` branch, and then the `fopen` function call reads the `flag` file, thus outputting the content of the file: `SSof{Time_of_Check_Time_of_Use_or_toctou_racing}`.

[(POC)](`challenge.sh`)