#!/usr/bin/env python
#coding:UTF-8

import socket
import sys
import os


ip_port = ('127.0.0.1',9990)
sk = socket.socket()
sk.connect(ip_port)


while True:
    cmd_file = input('Path:')
    cmd, file_path = cmd_file.split('|')
    print(cmd)
    print(file_path)
    file_name = os.path.basename(file_path)
    print(file_name)
    file_size = os.stat(file_path).st_size
    print(file_size)
    send_info = cmd+"|"+file_name+"|"+str(file_size)
    print(send_info)
    send_info_b = send_info.encode(encoding='utf-8')
    print(send_info_b)
    sk.sendall(send_info_b)
    sk.sendall(b'hahaha')
'''
    send_size = 0
    f = open(file_path,'rb')
    Flag = True
    while Flag:
        if send_size + 1024 > file_size:
            data = f.read(file_size-send_size)
            send_size = 0
            Flag = False
        else:
            data = f.read(1024)
            send_size += 1024
        sk.send(data)

    f.close()
'''
sk.close()


