# Challenge `Call Functions Again` writeup

- Vulnerability: Arbitrary memory write
- Where: In the `printf` function call
- Impact: It allows overwriting the GOT's `puts` entry to reference an arbitrary memory position (in this case, the `win` function)

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint in the `printf` call and running the binary, the stack pointer `esp` is then located in the beginning of the format string. By inspecting the stack's contents below the pointer, we can find the original location of `buffer` 7 registers (28 bytes) below it (the content will always match what was written by us).

2. In order to get the flag, an attacker can, for example, make use of the fact that the `puts` function has its address located in the global offset table (GOT), and replace that address to force a call to a custom address (in this case, the `win` function). In this situation, `puts`'s GOT address is `0x804c018` and points to `0x8049070`. Since the `win` function is located at `0x8049216`, we just need to replace the two least significant bytes.

3. By repeating the same process of the last challenge (byte counter overflow), we can build a format string (`\x19\xc0\x04\x08\x18\xc0\x04\x08\x45%138x%7$hhn%132x%8$hhn`) that points to the two least significant bytes and replaces them with `win`'s two least significant bytes, allowing us to run the function and get the flag: `SSof{You_GOT_me}`.

[(POC)](`call_functions.py`)