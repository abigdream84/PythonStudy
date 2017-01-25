#!/usr/bin/env python
#coding:UTF-8

import socketserver

class MyServer(socketserver.BaseRequestHandler):
    
    def setup(self):
        pass

    def handle(self):
        conn = self.request
        data = 'hello'
        data_b = data.encode(encoding='utf_8')
        conn.send(data_b)
        flag = True
        while flag:    
            mess = conn.recv(1024)
            mess_s = mess.decode('ascii')
            print(mess_s)
            if mess_s == '0':
                mess = 'hahahaha'
                mess_b = mess.encode(encoding='utf_8')
                conn.send(mess_b)
            elif mess_s == 'exit':
                break
            else:
                mess = 'sb'
                mess_b = mess.encode(encoding='utf_8')
                conn.send(mess_b)
        conn.close()


    def finish(self):
        pass



if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9998),MyServer)
    server.serve_forever()








