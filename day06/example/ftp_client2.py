#!/usr/bin/env python
#coding:UTF-8

#!/usr/bin/env python
#coding:utf-8


import socket
import sys
import os

ip_port = ('127.0.0.1',9999)
sk = socket.socket()
sk.connect(ip_port)

container = {'key':'','data':''}
while True:
    input_t = input('path:')
    cmd,path = input_t.split('|') 
    file_name = os.path.basename(path)
    print(file_name)
    file_size=os.stat(path).st_size
    print(file_size)
    file_info=cmd+"|"+file_name+'|'+str(file_size)
    file_info_b=file_info.encode(encoding='utf-8')
    print(file_info_b)
    sk.sendall(file_info_b)
    res_b = sk.recv(1024)
    res = res_b.decode('ascii')
    print(res)
    send_size = 0
    f= open(path,'rb')
    Flag = True
    while Flag:
        if send_size + 1024 >file_size:
            data = f.read(file_size-send_size)
            sk.send(data)
            send_size = 0
            Flag = False
            
        else:
            data = f.read(1024)
            send_size+=1024
            sk.send(data)
    f.close()
    
sk.close()




