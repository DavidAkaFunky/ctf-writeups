# Challenge ` Pickles in a seri(al)ous race` writeup

- Vulnerability: Race condition (lack of mutual exclusion) + Remote code execution in Pickle
- Where: Inside the `type_choice`'s if-elif code blocks
- Impact: It allows to write a file in `FREE` mode containing an encoded bash command, then read it in `CLASSY` mode using `pickle.loads()`, which executes the command

## Finding the vulnerability / Steps to reproduce

1. The Pickle package has [a known RCE exploit](https://davidhamann.de/2020/04/05/exploiting-python-pickle/) in the `pickle.loads()` function, which could be exploited to get the flag.
2. A naïve approach would be to, sequentially, write a file in `FREE` mode containing an encoded bash command, then attempt to read it in `CLASSY` mode using `pickle.loads()`, expecting it to execute the command. However, the `check_mode()` function clears the user's directory when the mode is changed, meaning that, in the second execution, there would be no file to be read.
3. The exploit requires modifying the naïve approach by keeping two parallel sessions - one in `FREE` mode and another in `CLASSY` mode -, and ensuring both reach the end of the `check_mode()` function before proceeding with the sequential execution of each mode.

[(POC)](`serial_race.py`)