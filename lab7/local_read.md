# Challenge `Simple Local Read` writeup

- Vulnerability: Arbitrary memory read
- Where: In the `printf` function call
- Impact: It allows reading `secret_value`

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint in the `printf` call and running the binary, the stack pointer `esp` is then located in the beginning of the format string. By inspecting the stack's contents below the pointer, we can find `secret_value` referenced 7 registers (28 bytes) below it.

2. This means we can print its value by sending a format string that prints the 6 registers below it in an arbitrary way, followed by a print of the content of what the 7th register references (`secret_value`), using, for example: `%08x.%08x.%08x.%08x.%08x.%08x.%s`.

3. Sending this format string returns the flag in the final value: `SSof{There_are_no_Secrets_in_stack}`.

[(POC)](`local_read.py`)