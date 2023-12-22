# Challenge `Calling Functions` writeup

- Vulnerability: Buffer overflow
- Where: In the `gets` call to `buffer`
- Impact: It allows the replacement of `fp`, which leads to accessing an arbitrary function

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint (for example, after the declaration of all variables in the `main` function), we can see, by calling `p &buffer` and `p &fp`, that `buffer`, which holds 32 bytes (i.e. `0x20`), is located at the memory address `0xffffcf3c` and `fp` is located at `0xffffcf5c`, meaning it's located immediately after `buffer`.

2. As such, to replace its value, an attacker only needs to send a string that is 36 bytes long and where the 4 last bytes are the `win` function's address, which we know, by calling `p &win`, is `0x080486f1`. No byte order manipulation seems to be needed, as `pwn`'s `p32` function seems to be generating the bytes using little-endian for us. 

3. The overflown value, `0x080486f1`, will overwrite `fp`'s value, allowing us to jump to the `win` function and win the game (and the flag: `SSof{Buffer_Overflow_function_pointers}`).

[(POC)](`functions.py`)