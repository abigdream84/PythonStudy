#!/usr/bin/env python
#coding:UTF-8

'''
from example import reflect1
reflect1.Fun1()
'''

aa = 'reflect1'
bb = 'Fun2'

moud = __import__(aa)
fun = getattr(moud,bb)
fun()








