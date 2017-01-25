#!/usr/bin/env python
#coding:UTF-8


import socket

ip_addr = ('127.0.0.1',9998)

client = socket.socket()

client.connect(ip_addr)

while True:
    mess = client.recv(1024)
    mess_s = mess.decode('ascii')
    print(mess_s)
    
    data = input('client:')
    data_b = data.encode(encoding='utf_8')
    client.send(data_b)
    if data == 'exit':
        break

client.close()




