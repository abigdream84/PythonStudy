#!/usr/bin/env python
#coding:UTF-8

'''
import pymysql

db = pymysql.connect("127.0.0.1","root","root","ebankdb")
cursor = db.cursor()
reCount = cursor.execute("select * from test")
data = cursor.fetchone()
print(reCount)
print(data)
cursor.scroll(3,mode='relative')
data = cursor.fetchone()
print(reCount)
print(data)
cursor.close()
db.close()
'''
'''
import pymysql

sql = "insert into test(id,name) values (%s,%s)"
params = (6,'yyy')

db = pymysql.connect(host="127.0.0.1",user="root",password="root",database="ebankdb")
cursor = db.cursor()
reCount = cursor.execute(sql,params)
db.commit()
#data = cursor.fetchall()
print(reCount)
#print(data)
cursor.close()
db.close()
'''
'''
import pymysql

sql = "delete from test where id=%s"
params = (6)

db = pymysql.connect(host="127.0.0.1",user="root",password="root",database="ebankdb")
cursor = db.cursor()
reCount = cursor.execute(sql,params)
db.commit()
#data = cursor.fetchall()
print(reCount)
#print(data)
cursor.close()
db.close()
'''
'''
import pymysql

sql = "update test set name = %s where id =%s"
params = ('ttt',6)

db = pymysql.connect(host="127.0.0.1",user="root",password="root",database="ebankdb")
cursor = db.cursor()
reCount = cursor.execute(sql,params)
db.commit()
#data = cursor.fetchall()
print(reCount)
#print(data)
cursor.close()
db.close()
'''

import pymysql

sql = "insert into test(id,name) values(%s,%s)"
params = [
          (8,'ppp'),
          (9,'bbb')]

db = pymysql.connect(host="127.0.0.1",user="root",password="root",database="ebankdb")
cursor = db.cursor()
reCount = cursor.executemany(sql,params)
db.commit()
#data = cursor.fetchall()
print(reCount)
#print(data)
cursor.close()
db.close()











