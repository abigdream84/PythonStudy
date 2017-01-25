#!/usr/bin/env python
#coding:UTF-8


from talk_demo.utility.MySqlHelper import MySqlHelper

class indextb(object):
    
    def __init__(self):
        self.__helper = MySqlHelper()
    
    def __getCount(self):
        sql = 'select count(*) from indextb'
        row_count = self.__helper.select(sql)[0][0]
        return row_count
   
    def chkWord(self,mess):    
        sql2 = 'select * from indextb'
        data = self.__helper.select(sql2)
        row = self.__getCount()
        mess = mess.decode('ascii')
        print(mess)
        print(type(mess))
        for item in range(row):
#            print(data[item][1])
#            print(type(data[item][1]))
            if mess.__contains__(data[item][1]):
                return data[item][2]
            item += item
        

'''
aa = indextb()
res = aa.chkWord('hello')
print(res)

'''




