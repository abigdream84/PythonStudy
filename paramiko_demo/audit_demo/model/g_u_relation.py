#!/usr/bin/env python
#coding:UTF-8

from audit_demo.utility.MySqlHelper import MySqlHelper

class g_u_relation(object):
    def __init__(self):
        self.__helper = MySqlHelper()
    
    def get_uid(self,username):
        sql = 'select u_id from u_table where u_name = %s' 
        try:
            u_id = self.__helper.select(sql,username)[0][0]  
            return u_id 
        except Exception as e:
            print(e)
            return False
            
        
    
    def get_gid(self,gpname):
        sql = 'select g_id from g_table where g_name = %s' 
        try:
            g_id = self.__helper.select(sql,gpname)[0][0] 
            return g_id  
        except Exception as e:
            print(e)
            return False 
    
    def add_u_g(self,username,gpname):
        uid = str(self.get_uid(username))
        gid = str(self.get_gid(gpname))
        sql = 'insert into g_u_relation(f_g_id,f_u_id) values(%s , %s)'
        params = (gid,uid)
        try:
            self.__helper.insert_one(sql,params)
        except Exception as e:
            print(e)
            return False
    
    def get_u_g_id(self, username):
        uid = str(self.get_uid(username))
        sql = 'select g_u_id from g_u_relation where f_u_id = %s'
        params = (uid)
        try:
            tmplist = self.__helper.select(sql,params)
            u_g_id_list = []
            for i in tmplist:
                t = i[0]
                u_g_id_list.append(t)
            return u_g_id_list
        except Exception as e:
            print(e)
            return False
        
    def get_g_u_id(self, gpname):
        gid = str(self.get_gid(gpname))
        sql = 'select g_u_id from g_u_relation where f_g_id = %s'
        params = (gid)
        try:
            tmplist = self.__helper.select(sql,params)
            g_u_id_list = []
            for i in tmplist:
                t = i[0]
                g_u_id_list.append(t)
            return g_u_id_list
        except Exception as e:
            print(e)
            return False
    
    def del_u_g(self, username):
        sql = 'delete from g_u_relation where g_u_id = %s'
        if not self.get_u_g_id(username):
            print('No relations of %s in g_u_relation table.' %username)
        else:
            u_g_id_list = self.get_u_g_id(username)
            try:
                for i in u_g_id_list:
                    params = i
                    self.__helper.delete(sql,params)
            except Exception as e:
                print(e)  
    
    def del_g_u(self, gpname):
        sql = 'delete from g_u_relation where g_u_id = %s'
        if not self.get_g_u_id(gpname):
            print('No relations of %s in g_u_relation table.' %gpname)
        else:
            g_u_id_list = self.get_g_u_id(gpname)
            try:
                for i in g_u_id_list:
                    params = i
                    self.__helper.delete(sql,params)
            except Exception as e:
                print(e)           
    
    
        
        

'''
t=g_u_relation()
t.add_u_g('user1', 'gp2')
#print(t.del_g_u('gp1'))
'''



