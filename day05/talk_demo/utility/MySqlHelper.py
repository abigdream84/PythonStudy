#!/usr/bin/env python
#coding:UTF-8

import pymysql
import talk_demo.settings

class MySqlHelper(object):
    
    def __init__(self):
        self.__db_conn = talk_demo.settings.db_conn
    
    def insert(self,*args):
        db = pymysql.connect(**self.__db_conn)
        cursor = db.cursor()
        cursor.executemany(*args)
        db.commit()
        cursor.close()
        db.close()
        
    def select(self,*args):
        db = pymysql.connect(**self.__db_conn)
        cursor = db.cursor()
        cursor.execute(*args)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def update(self,*args):
        db = pymysql.connect(**self.__db_conn)
        cursor = db.cursor()
        cursor.execute(*args)
        db.commit()
        cursor.close()
        db.close()

    def delete(self,*args):
        db = pymysql.connect(**self.__db_conn)
        cursor = db.cursor()
        cursor.execute(*args)
        db.commit()
        cursor.close()
        db.close()


        


'''    
    def chkWord(self,mess,dbname):
        db = pymysql.connect(**self.__db_conn)
        cursor = db.cursor()
        sql1 = 'select count(*) from %s'
        params = dbname
        print(params)
        print(type(params))
        
   
        cursor.execute(sql1,params)
        row_count = cursor.fetchall()[0][0]
        print(row_count)
      
             
        sql2 = 'select * from %s'
        params = dbname
        cursor.execute(sql2,params)
        for item in range(row_count):
            data = cursor.fetchone()
            if mess.__contains__(data[chkcol]):
                return data[rescol]
            item += item
        cursor.close()
        db.close()

'''
        
'''
handle = MySqlHelper()
#sql = 'delete from test where id = %s'
#params = (2,)
res = handle.chkWord('what is your name','indextb')
print(res)
#print(handle.selectOne())
'''


       
        