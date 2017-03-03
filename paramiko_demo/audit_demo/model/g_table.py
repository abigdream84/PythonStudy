#!/usr/bin/env python
#coding:UTF-8

from audit_demo.utility.MySqlHelper import MySqlHelper
from audit_demo.model.g_u_relation import g_u_relation
from audit_demo.model.s_g_u_relation import s_g_u_relation

class g_table(object):
    def __init__(self):
        self.__helper = MySqlHelper()
    
    def add_grp(self,gpname):
        sql = 'insert into g_table(g_name) values(%s)'
        params = (gpname,)
        try:
            self.__helper.insert_one(sql,params)
            return True
        except Exception as e:
            print(e)
            return False
        
    def get_grp(self,gpname):
        sql = 'select g_id from g_table where g_name = %s' 
        try:
            g_id = self.__helper.select(sql,gpname)[0][0]   
        except Exception as e:
            print(e)
        return g_id
    
    def upd_grp(self,gpname_old,gpname_new):
        sql = 'update g_table set g_name = %s where g_name = %s'
        params = (gpname_new, gpname_old)
        try:
            self.__helper.update(sql,params)
        except Exception as e:
            print(e)
    
    def del_grp(self, gpname):
        sql = 'delete from g_table where g_name=%s'
        g_u_handle = g_u_relation()
        s_g_u_handle = s_g_u_relation
        if g_u_handle.get_g_u_id(gpname):
            g_u_handle.del_g_u(gpname)
        if s_g_u_handle.get_s_g_id(gpname):
            s_g_u_handle.del_s_g(gpname)
        try:
            self.__helper.delete(sql,gpname)
        except Exception as e:
            print(e)

'''
t=g_table()
#t.upd_grp('gp4','gp2')
#t.add_grp('gp2')
#t.del_grp('gp2')
'''


