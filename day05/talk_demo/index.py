#!/usr/bin/env python
#coding:UTF-8

import socketserver
from talk_demo.model.indextb import indextb

class MyServer(socketserver.BaseRequestHandler):
    
    def setup(self):
        pass

    def handle(self):
        conn = self.request
        indextb_handle = indextb()
        data = 'Hello, I am talk! Nice to meet you!'
        data_b = data.encode(encoding='utf_8')
        conn.send(data_b)
        flag = True
        while flag:    
            mess = conn.recv(1024)
            mess_s = mess.decode('ascii')
            print(mess_s)
            if mess_s == 'exit':
                break
            else:
                res = indextb_handle.chkWord(mess)
                if not res:
                    mess = 'I do not know what you are talking about!'
                    mess_b = mess.encode(encoding='utf_8')
                    conn.send(mess_b)
                else:
                    mess = res
                    mess_b = mess.encode(encoding='utf_8')
                    conn.send(mess_b)
              
        conn.close()


    def finish(self):
        pass



if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('127.0.0.1',9998),MyServer)
    server.serve_forever()









