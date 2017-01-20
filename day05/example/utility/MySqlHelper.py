#!/usr/bin/env python
#coding:UTF-8

import pymysql


class MySqlHelper(object):
    
    def __init__(self):
        pass
    
    def fetchOne(self,sql):
        db = pymysql.connect(host='127.0.0.1',user='root',password='root',database='ebankdb')
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data
    
    def fetchAll(self,sql):
        db = pymysql.connect(host='127.0.0.1',user='root',password='root',database='ebankdb')
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data
    
    def query(self,sql,params):
        db = pymysql.connect(host='127.0.0.1',user='root',password='root',database='ebankdb')
        cursor = db.cursor()
        cursor.execute(sql,params)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data
        
    def execute(self,sql,params):
        db = pymysql.connect(host='127.0.0.1',user='root',password='root',database='ebankdb')
        cursor = db.cursor()
        cursor.execute(sql,params)
        db.commit()
        cursor.close()
        db.close()
        
    def executemany(self,sql,params):
        db = pymysql.connect(host='127.0.0.1',user='root',password='root',database='ebankdb')
        cursor = db.cursor()
        cursor.executemany(sql,params)
        db.commit()
        cursor.close()
        db.close()





