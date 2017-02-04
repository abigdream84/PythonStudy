#!/usr/bin/env python
#coding:UTF-8

import threading
import time

def producer():
    print('waiting for sb')
    event.wait()
    event.clear()
    print('sb is coming for baozi')
    print('making a baozi for sb')
    time.sleep(3)
    print('baozi is ready')
    event.set()

def consumer():
    print('go to buy baozi')
    event.set()
    print('waiting for baozi to be ready')
    time.sleep(2)
    event.wait()
    event.clear()
    print('thanks')
    
    
event = threading.Event()
p = threading.Thread(target=producer)
c = threading.Thread(target=consumer)
p.start()
c.start()








