# Challenge `Write Specific Byte` writeup

- Vulnerability: Arbitrary memory write
- Where: In the `printf` function call
- Impact: It allows writing on `target`

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint in the `printf` call and running the binary, the stack pointer `esp` is then located in the beginning of the format string. By inspecting the stack's contents below the pointer, we can find the original location of `buffer` 7 registers (28 bytes) below it (the content will always match what was written by us).

2. The source code requires that the most significant byte of `target` equals `2`, so we can write directly on that byte by finding `target`'s first byte (i.e., the least significant one, since the memory is addressed using little endian) in the 7th register and adding 3 to that value.

3. After that, we must ensure that the written value is `2`, but the byte counter is already at `4`. To fix that, we must overflow it: if we add `254`, the written value will be `(4 + 254) % 256 = 2`.

4. The final string, `\x47\xc0\x04\x08%323x%7$n`, overwrites `target` with `2`, allowing us to get the flag: `SSof{And_write_big_numbers}`.

[(POC)](`write_specific_byte.py`)