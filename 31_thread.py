#!/usr/bin/env python3

import threading

def run():
    cur = threading.current_thread()
    main = threading.main_thread()
    print('in child: name[%s], main name[%s]' % (cur.name, main.name))

if __name__ == '__main__':
    print('in main: name[%s]' % threading.current_thread().name)
    p = threading.Thread(target=run, name='child1')
    p.start()
    p.join()

