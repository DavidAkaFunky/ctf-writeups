# Challenge `Return Address Again` writeup

- Vulnerability: Arbitrary memory write
- Where: In the `printf` function call
- Impact: It allows overwriting the `vuln`'s return address to reference an arbitrary memory position (in this case, the `win` function)

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint in the `printf` call and running the binary, the stack pointer `esp` is then located in the beginning of the format string. By inspecting the stack's contents below the pointer, we can find the original location of `buffer` 7 registers (28 bytes) below it (the content will always match what was written by us).

2. In this challenge, the stack's location seems to change between machines, as seen by the location of `buffer` and the `eip` register (which points to `vuln`'s return address). However, their distance remains the same: 144 bytes. This means we can obtain `eip`'s location by first sending a `%08x` payload to obtain `buffer`'s location and then adding the aforementioned offset.

3. From then on, by repeating the same process of the last challenge (byte counter overflow), we can build a format string that points to the `eip` register's two least significant bytes and replaces them with `win`'s two least significant bytes, allowing us to enter the `win` function after the end of `vuln` and get the flag: `SSof{Returning_to_the_same_old_things}`.

[(POC)](`return.py`)