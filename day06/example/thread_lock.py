#!/usr/bin/env python
#coding:UTF-8
'''
import threading
import time

num = 0
def run():
    time.sleep(1)
    global num
    lock.acquire()
    num += 1
    print(num)
    lock.release()
    


lock = threading.Lock()
for i in range(100):
    t = threading.Thread(target=run)
    t.start()
'''

import threading
import time

num = 0
def run():

    global num
    samp.acquire()
    time.sleep(0.1)
    num += 1
    print('%s' %num)
    samp.release()
    


samp = threading.BoundedSemaphore(4)
for i in range(100):
    t = threading.Thread(target=run)
    t.start()

