#!/usr/bin/env python3.5
#coding:UTF-8

import socket

ip_addr = ('127.0.0.1',9999)

sk = socket.socket()

sk.bind(ip_addr)
sk.listen(5)
while True:
    conn, addr = sk.accept()
    print(conn)
    print(addr)
    mess = 'hello'
    conn.send(mess.encode(encoding='utf_8'))
    flag = True
    while flag:
        data = conn.recv(1024)
        data_str = data.decode('ascii')
        print(data_str)
        if data_str == 'exit':
            flag = False
        elif data_str == '0':
            mess = 'ffffff'
            conn.send(mess.encode(encoding='utf_8'))
        else:
            mess = 'tttttt'
            conn.send(mess.encode(encoding='utf_8'))
    
    conn.close()



