#!/usr/bin/python3
for aplhabets in range(ord('a'), ord('z') + 1):
    if chr(aplhabets) == 'e' or chr(aplhabets) == 'q':
        continue
    else:
        print("{:c}".format(chr(aplhabets)), end="")
