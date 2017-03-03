#!/usr/bin/env python
#coding:UTF-8

import pymysql
import audit_demo.settings

class MySqlHelper(object):
    
    def __init__(self):
        self.__db_conn = audit_demo.settings.db_conn
    
    def insert_one(self,*args):
        db = pymysql.connect(**self.__db_conn)
        cursor = db.cursor()
        cursor.execute(*args)
        db.commit()
        cursor.close()
        db.close()
    
    def insert_many(self,*args):
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
handle = MySqlHelper()
sql = 'insert into g_u_relation(f_g_id,f_u_id) values(%s , %s)'
#params = ('5','1')

handle.insert(sql, ('5','1'))

'''

       
        