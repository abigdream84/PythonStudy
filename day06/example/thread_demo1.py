#!/usr/bin/env python
#coding:UTF-8

'''
from threading import Thread
import time

class MyThread(Thread):
    def run(self):
        print('mythread')
        Thread.run(self)

def Foo(var):
    for i in range(5):
        print(var,str(i))
        time.sleep(1)


print('start')
t1 = MyThread(target=Foo, args=('haha',))
t1.start()
print('end')
'''
'''
from threading import Thread
from queue import Queue
import time

class Producer(Thread):
    def __init__(self,name,queue):
        self.__Name = name
        self.__Queue = queue
        super(Producer,self).__init__()
    
    def run(self):
        while True:
            if self.__Queue.full():
                time.sleep(1)
            else:
                self.__Queue.put('baozi')
                print('%s made a baozi' %(self.__Name,))
                time.sleep(1)
        #Thread.run(self)

class Consumer(Thread):
    def __init__(self,name,queue):
        self.__Name = name
        self.__Queue = queue
        super(Consumer,self).__init__()

    def run(self):
        while True:
            if self.__Queue.empty():
                time.sleep(1)
            else:
                self.__Queue.get()
                print('%s get a baozi' %(self.__Name,))
                time.sleep(1)
        #Thread.run(self)

que = Queue(20)

for item in range(2):
    name = 'p%d' %(item,)
    temp = Producer(name,que)
    temp.start()

for item in range(2):
    name = 'c%d' %(item,)
    temp = Consumer(name,que)
    temp.start()
'''

import threading
import queue
import random
import time

def producer(name,que):
    while True:
        if que.qsize() < 3:
            que.put('baozi')
            time.sleep(random.randrange(3))
            print('%s make a baozi!!!!!!' %name)
        else:
            print('There are 3 baozi.')
            time.sleep(1)
    
def consumer(name,que):
    while True:
        try:
            que.get_nowait()
            time.sleep(random.randrange(2))
            print('%s take a baozi.....' %name)
        except Exception:
            print('There are no baozi???????')
            time.sleep(1)
        

que = queue.Queue(10)
p1 = threading.Thread(target=producer, args=('p1',que))
p2 = threading.Thread(target=producer, args=('p2',que))
p1.start()
p2.start()

c1 = threading.Thread(target=consumer, args=('c1',que)) 
c2 = threading.Thread(target=consumer, args=('c2',que)) 
c1.start()
c2.start()
    
    
    
    





