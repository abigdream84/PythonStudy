#!/usr/bin/env python
#coding:UTF-8


import socketserver
import os

class MyFtpServer(socketserver.BaseRequestHandler):
    
    def handle(self):
        base_dir = '/tmp'
        conn = self.request
        print('Connected...')
        while True:
            data = conn.recv(1024)
            print(data)
            if not data: break
        print(data)

        
'''        
        while True:
            pre_data_b = conn.recv(1024)
            print(pre_data_b)
            pre_data = pre_data_b.decode('ascii')
            print(pre_data)
            cmd,file_name,file_size = pre_data.split('|')
            file_dir = os.path.join(base_dir, file_name)
            f = open(file_dir,'wb')
            recv_size = 0
            Flag = True
            while Flag:
                if int(file_size) > recv_size:
                    data = conn.recv(1024)
                    recv_size += len(data)
                else:
                    recv_size = 0
                    Flag = False
                    continue
                f.write(data)
        f.close()
        print('Upload successed!')
        
'''
instance = socketserver.ThreadingTCPServer(('127.0.0.1',9990),MyFtpServer)
instance.serve_forever()

                               



