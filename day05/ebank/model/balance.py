#!/usr/bin/env python
#coding:UTF-8

from ebank.utility.MySqlHelper import MySqlHelper

class balance(object):
    
    def __init__(self):
        self.__helper = MySqlHelper()
    
    def query(self,user_id):
        sql = 'select balance from balance where id = %s'
        balance = self.__helper.select(sql,user_id)[0][0]
        return balance

    def __getBalance(self,user_id):
        sql = 'select balance from balance where id = %s' 
        try:
            user_balance = self.__helper.select(sql,user_id)[0][0]   
        except Exception as e:
            print(e)
        return user_balance

    def __addBalance(self,user_id,amount):
        user_balance = self.__getBalance(user_id)
        user_balance += amount
        sql = 'update balance set balance = %s where id = %s'
        params = (user_balance, user_id)
        try:
            self.__helper.update(sql,params)
        except Exception as e:
            print(e)
        
    def __desBalance(self,user_id,amount):
        user_balance = self.__getBalance(user_id)
        user_balance -= amount
        sql = 'update balance set balance = %s where id = %s'
        params = (user_balance, user_id)
        try:
            self.__helper.update(sql,params)
        except Exception as e:
            print(e)

    def drawMoney(self,user_id,amount):
        balance = self.__getBalance(user_id)
        try:
            amount = float(amount)
        except ValueError as e:
            print(e)
            return 2
            
        if amount > balance:
            return 1
        else:
            self.__desBalance(user_id, amount)
            return 0

    def depositMoney(self,user_id,amount):
        try:
            amount = float(amount)
        except ValueError as e:
            print(e)
            return 2
        
        self.__addBalance(user_id, amount)
        return 0

    def transfer(self,user_id, user_des, amount):
        balance = self.__getBalance(user_id)
        try:
            amount = float(amount)
        except ValueError as e:
            print(e)
            return 2
        
        if amount > balance:
            return 1
        else:
            self.__desBalance(user_id, amount)
            self.__addBalance(user_des, amount)
            return 0
       


