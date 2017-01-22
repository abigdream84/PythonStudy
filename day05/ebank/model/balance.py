#!/usr/bin/env python
#coding:UTF-8

from ebank.utility.MySqlHelper import MySqlHelper

class balance(object):
    
    def __init__(self):
        self.__helper = MySqlHelper()
    
    def query(self,user_id):
        sql = 'select balance from balance where id = %s'
        balance = self.__helper.select(sql,user_id)
        return balance



