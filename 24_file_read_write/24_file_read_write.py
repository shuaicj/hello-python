#!/usr/bin/env python3

from functools import partial

FILE_READ = './file_for_read.txt'
FILE_WRITE = './file_for_write.txt'

print('--------------------------')

with open(FILE_READ) as fr:
    print(fr.readline())

print('--------------------------')

with open(FILE_READ) as fr:
    print(fr.readlines())

print('--------------------------')

with open(FILE_READ) as fr:
    for line in fr:
        print(line)

print('--------------------------')

with open(FILE_READ) as fr:
    two_chars = fr.read(2)
    while two_chars:
        print(two_chars)
        two_chars = fr.read(2)

print('--------------------------')

with open(FILE_READ, 'rb') as fr:
    two_bytes = fr.read(2)
    while two_bytes:
        print(two_bytes)
        two_bytes = fr.read(2)

print('--------------------------')

with open(FILE_WRITE, 'w') as fw:
    fw.writelines(['line a\n', 'line b\n', 'line c\n'])

with open(FILE_WRITE) as fw:
    print(fw.readlines())

print('--------------------------')

with open(FILE_WRITE, 'w') as fw:
    fw.write('line a\n')
    fw.write('line b\n')
    fw.write('line c\n')

with open(FILE_WRITE) as fw:
    print(fw.readlines())

print('--------------------------')
