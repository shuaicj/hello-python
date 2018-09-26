#!/usr/bin/env python3

from multiprocessing import Process
import os

def run():
    print('in child: pid[%s], ppid[%s]' % (os.getpid(), os.getppid()))

if __name__ == '__main__':
    print('in parent: pid[%s]' % os.getpid())
    p = Process(target=run)
    p.start()
    p.join()

