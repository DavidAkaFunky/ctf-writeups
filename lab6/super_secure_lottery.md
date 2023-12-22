# Challenge `Super Secure Lottery` writeup

- Vulnerability: Buffer overflow
- Where: In the `read` call to `guess`
- Impact: It allows the replacement of `prize` (in our case, to the same value as `guess`'s first 8 bytes)

## Finding the vulnerability / Steps to reproduce

1. After setting a breakpoint after the declaration of `guess` in the `run_lottery` function, we can see, by calling `p &guess` and `p prize` (no pointer operator needed because `prize` is already a pointer), that `guess`, which holds 64 bytes (i.e. `0x40`), is located at the memory address `0xffffcf14` and `prize` is located at `0xffffcf44`, meaning it's effectively located inside `guess`' allocated memory (48 bytes, `0x30`, after `guess`' pointer).

2. To win the lottery, we must set `guess`' first 8 bytes to be the same as `prize`'s. As such, a payload containing an 8-byte string (let's call it `X`), followed by 40 random bytes, then `X` again, and finally a `\n` to send the command will successfully overwrite `prize`'s previously randomly generated value to `X`, which is the same value `guess`' value was set to, leading us to win the lottery (and the flag: `SSof{You_will_N3V3R_guess_a_totally_random_lottery}`).

[(POC)](`super_secure_lottery.py`)