#!/usr/bin/env python3

import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True)
print('exit code:', result.returncode)
print(result)
