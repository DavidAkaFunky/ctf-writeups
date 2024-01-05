# Challenge `Write Big Numbers` writeup

- Vulnerability: Arbitrary memory write
- Where: In the `printf` function call
- Impact: It allows writing on `target`

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint in the `printf` call and running the binary, the stack pointer `esp` is then located in the beginning of the format string. By inspecting the stack's contents below the pointer, we can find the original location of `buffer` 7 registers (28 bytes) below it (the content will always match what was written by us).

2. By repeating the same process of the last challenge (byte counter overflow) in each of `target`'s address' bytes, we can build a format string (`\x47\xc0\x04\x08\x46\xc0\x04\x08\x45\xc0\x04\x08\x44\xc0\x04\x08%206x%7$hhn%207x%8$hhn%273x%9$hhn%305x%10$hhn`) that allows us to get the flag: `SSof{And_write_Very_BIIIIIG_numbers}`.

[(POC)](`write_big_number.py`)