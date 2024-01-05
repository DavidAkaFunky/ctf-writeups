# Challenge `Short Local Read` writeup

- Vulnerability: Arbitrary memory read
- Where: In the `printf` function call
- Impact: It allows reading `secret_value`

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint in the `printf` call and running the binary, the stack pointer `esp` is then located in the beginning of the format string. By inspecting the stack's contents below the pointer, we can find `secret_value` referenced 7 registers (28 bytes) below it.

2. Unlike the previous challenge, the sent format string must be at most 5 bytes long, so the same format string cannot be used. An alternative involves immediately skipping to the 7th register below `%7` and print what it references (`$s`), yielding a 4 byte string: `%7$s`.

3. Sending this format string returns the flag: `SSof{Positional_arguments_FTW}`.

[(POC)](`local_short_read.py`)