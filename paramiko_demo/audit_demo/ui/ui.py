#!/usr/bin/env python
#coding:UTF-8

from audit_demo.model.s_table import s_table



def get_ser_list(username):
    s_handle = s_table()
    s_list = s_handle.get_u_s_list(username)
    return s_list
    
def pri_ser(username):
    s_list = get_ser_list(username)
    j = 1
    ser_dic = {}
    for i in s_list:
        print('%s. %s'  %(j,i))
        ser_dic[j]=i
        j+=1
    return ser_dic



#def con_ser(serip):

  
if __name__ == '__main__':
    ser_dic = pri_ser('user1')
    inp = input('please choose the server:')
    ser_ip = ser_dic[int(inp)]
    

