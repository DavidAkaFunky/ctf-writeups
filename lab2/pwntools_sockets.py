from pwn import *

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23055

s = remote(SERVER, PORT, timeout=10000)
target = int(s.recvline_contains(b"until you get to").split()[-1][:-1])
while True:
    current = int(s.recvline_contains(b"CURRENT").split()[2][:-1])
    s.recvline_contains(b"FINISH")
    if current == target:
        s.sendline(b"FINISH")
        print(s.recvline())
        break
    s.sendline(b"MORE")