#!/usr/bin/env python
#coding:UTF-8


import pymysql

db = pymysql.connect("127.0.0.1","root","root","ebankdb")
cursor = db.cursor()
reCount = cursor.execute("select * from test")
data = cursor.fetchall()
print(reCount)
print(data)
cursor.close()
db.close()


















