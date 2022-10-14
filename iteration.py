#!/usr/bin/python3
from itertools import dropwhile


with open('/etc/passwd', 'r') as f:
    for line in dropwhile(lambda line : line.startswith("#"), f):
        print(line)
