#!/usr/bin/env python
#coding:UTF-8

from example.utility.MySqlHelper import MySqlHelper

class test(object):
    
    def __init__(self):
        self.__handle = MySqlHelper()
    
    def selectAll(self):
        sql = 'select * from test'
        data = self.__handle.fetchAll(sql)
        return data

    def select(self,params):
        sql = 'select * from test where id = %s'
        data = self.__handle.query(sql,params)
        return data

    def insertOne(self,params):
        sql = 'insert into test(id,name) values(%s,%s)'
        self.__handle.execute(sql, params)
        
    def insertMany(self,params):
        sql = 'insert into test(id,name) values(%s,%s)'
        self.__handle.executemany(sql, params)

    def deleteId(self,params):
        sql = 'delete from test where id=%s'
        self.__handle.execute(sql, params)







