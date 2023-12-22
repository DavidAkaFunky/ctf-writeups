# Challenge `Match an Exact Value` writeup

- Vulnerability: Buffer overflow
- Where: In the `gets` call to `buffer`
- Impact: It allows the replacement of `test`

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint (for example, after the declaration of all variables), we can see, by calling `p &buffer` and `p &test`, that `buffer`, which holds 64 bytes (i.e. `0x40`), is located at the memory address `0xffffcf6c` and `test` is located at `0xffffcfac`, meaning it's located immediately after `buffer`.

2. As such, to replace its value, an attacker only needs to send a string that is 68 bytes long and where the 4 last bytes are `0x61626364`. No byte order manipulation seems to be needed, as `pwn`'s `p32` function seems to be generating the bytes using little-endian for us. 

3. The overflown value, `0x61626364`, will overwrite `test`'s value and allow us to win the game (and the flag: `SSof{Buffer_Overflow_can_change_values_to_wh4t3v3r_you_want}`).

[(POC)](`match.py`)