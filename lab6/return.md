# Challenge `Return Address` writeup

- Vulnerability: Buffer overflow
- Where: In the `gets` call to `buffer`
- Impact: It allows the replacement of the `challenge` function's saved return address

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint after the declaration of `buffer` inside the `challenge` function, we can see, by calling `p &buffer`, that `buffer`, which holds 10 bytes (i.e. `0xa`), is located at the memory address `0xffffcf66`. However, after calling `info f`, we know `eip` is at `0xffffcf7c`, i.e., 22 bytes (`0x16`) after `buffer`, meaning they are not contiguously saved.

2. A first (naïve) attempt involves sending any string that is 26 bytes long (which will overflow `ebx`, located at `0xffffcf74`, and `ebp`, located at `0xffffcf78`) and and where the 4 last bytes are the `win` function's address, which we know, by calling `p &win`, is `0x080486f1`. No byte order manipulation seems to be needed, as `pwn`'s `p32` function seems to be generating the bytes using little-endian for us. 

3. The overflown value, `0x080486f1`, will overwrite `eip`'s value, allowing us to return to the `win` function, instead of `main`, which was the one that called `challenge`, and win the game (and the flag: `SSof{Overflow_of_saved_r37urn_address}`). This also tells us that, in this situation, overwriting `ebx` and `ebp`'s values didn't turn out to be a problem, so saving those values in our buffer to preserve their integrity was not necessary.

[(POC)](`return.py`)