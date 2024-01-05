# Challenge `Write Specific Value` writeup

- Vulnerability: Arbitrary memory write
- Where: In the `printf` function call
- Impact: It allows writing on `target`

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint in the `printf` call and running the binary, the stack pointer `esp` is then located in the beginning of the format string. By inspecting the stack's contents below the pointer, we can find the original location of `buffer` 7 registers (28 bytes) below it (the content will always match what was written by us).

2. If we write, in the first position, the location of `target`, we can then write on `target` by calling `$d` in the 7th register after the format string (where `target`'s address was written), like so: `\x40\xc0\x04\x08%7$n`. `target` will, however, be overwritten with `4` (the number of bytes before `%7$n` in the format string), so we must enter 323 additional bytes before `%7$n`, using, for example, the padding operator: `%323x`.

3. The final string, `\x40\xc0\x04\x08%323x%7$n`, overwrites `target` with `327`, allowing us to get the flag: `SSof{And_you_can_write_what_you_want}`.

[(POC)](`match_write.py`)