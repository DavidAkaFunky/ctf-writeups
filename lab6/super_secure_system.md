# Challenge `Return Address` writeup

- Vulnerability: Buffer overflow
- Where: In the `strcmp` call from `password` to `buffer`, where `password` is longer than `buffer`
- Impact: It allows the replacement of the `challenge` function's saved return address

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint after the declaration of `buffer` inside the `challenge` function, we can see, by calling `p &buffer`, that `buffer`, which holds 32 bytes (i.e. `0x20`), is located at the memory address `0xffffced0`. However, after calling `info f`, we know `eip` is at `0xffffcefc`, i.e., 48 bytes (`0x2c`) after `buffer`, meaning they are not contiguously saved.

2. A first (naïve) attempt involves sending any string that is 48 bytes long (which will overflow `ebx`, located at `0xffffcef4`, and `ebp`, located at `0xffffcef8`) and and where the 4 last bytes are the first line of the `if` block in the `main` function, which we know, by calling `disassemble main`, is `0x080487d9`. No byte order manipulation seems to be needed, as `pwn`'s `p32` function seems to be generating the bytes using little-endian for us. 

3. The overflown value, `0x080487d9`, will overwrite `eip`'s value, but won't return the expected result, because the value of `ebp` is used later to calculate the address of the format string to be loaded in the `printf` call. To fix this, we can preserve its value (`0x0804a000`, obtained by calling `info registers`) and try again.

4. Once again, the result is not returned, because the `strcpy` will end the copy at `0x0804a000`'s final byte (`\0`, the string termination byte). This can be fixed by changing the written value to `0x0804a001`, with the minor side effect of moving the start of the format string loading to the second character.

5. After these fixes, the return to the `printf` inside the `if` block is successful (meaning overwriting the value of `ebp` was not problematic), and the flag is then displayed: `SSof{Jump_to_wh3r3v3r_you_want}`.

[(POC)](`super_secure_system.py`)