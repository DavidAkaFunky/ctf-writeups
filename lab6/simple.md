# Challenge `Simple Overflow` writeup

- Vulnerability: Buffer overflow
- Where: In the `gets` call to `buffer`
- Impact: It allows the replacement of `test`

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint (for example, after the declaration of all variables), we can see, by calling `p &buffer` and `p &test`, that `buffer`, which holds 128 bytes (i.e. `0x80`), is located at the memory address `0xffffcf1c` and `test` is located at `0xffffcf9c`, meaning it's located immediately after `buffer`.

2. As such, to replace its value, an attacker only needs to send a string over 128 bytes long, with the overflown value being anything other than 0, thus overwriting `test`'s value and allowing us to win the game (and the flag: `SSof{Buffer_Overflow_and_you_can_control_local_variables}`).

[(POC)](`simple.py`)