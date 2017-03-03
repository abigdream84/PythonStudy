#!/usr/bin/env python
#coding:UTF-8

from audit_demo.utility.MySqlHelper import MySqlHelper

class s_g_u_relation(object):
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

    def get_sid(self,serip):
        sql = 'select s_id from s_table where s_ip = %s' 
        try:
            s_id = self.__helper.select(sql,serip)[0][0] 
            return s_id  
        except Exception as e:
            print(e)
            return False
    
    def add_s_g(self,serip,gpname):
        sid = str(self.get_sid(serip))
        gid = str(self.get_gid(gpname))
        sql = 'insert into s_g_u_relation(f_s_id,f_g_id) values(%s , %s)'
        params = (sid,gid)
        try:
            self.__helper.insert_one(sql,params)
        except Exception as e:
            print(e)
            return False
        
    def add_s_u(self,serip,username):
        sid = str(self.get_sid(serip))
        uid = str(self.get_uid(username))
        sql = 'insert into s_g_u_relation(f_s_id,f_u_id) values(%s , %s)'
        params = (sid,uid)
        try:
            self.__helper.insert_one(sql,params)
        except Exception as e:
            print(e)
            return False    

    def get_s_u_g_id(self, serip):
        sid = str(self.get_sid(serip))
        sql = 'select s_g_u_id from s_g_u_relation where f_s_id = %s'
        params = (sid)
        try:
            tmplist = self.__helper.select(sql,params)
            s_u_g_id_list = []
            for i in tmplist:
                t = i[0]
                s_u_g_id_list.append(t)
            return s_u_g_id_list
        except Exception as e:
            print(e)
            return False
        
    def get_s_g_id(self, gpname):
        gid = str(self.get_gid(gpname))
        sql = 'select s_g_u_id from s_g_u_relation where f_g_id = %s'
        params = (gid)
        try:
            tmplist = self.__helper.select(sql,params)
            s_g_id_list = []
            for i in tmplist:
                t = i[0]
                s_g_id_list.append(t)
            return s_g_id_list
        except Exception as e:
            print(e)
            return False
  
    def get_s_u_id(self, username):
        uid = str(self.get_uid(username))
        sql = 'select s_g_u_id from s_g_u_relation where f_u_id = %s'
        params = (uid)
        try:
            tmplist = self.__helper.select(sql,params)
            s_u_id_list = []
            for i in tmplist:
                t = i[0]
                s_u_id_list.append(t)
            return s_u_id_list
        except Exception as e:
            print(e)
            return False
    
    def get_s_u_ser(self, username):
        uid = str(self.get_uid(username))
        sql = 'select f_s_id from s_g_u_relation where f_u_id = %s'
        params = (uid)
        try:
            tmplist = self.__helper.select(sql,params)
            s_u_list = []
            for i in tmplist:
                t = i[0]
                s_u_list.append(t)
            return s_u_list
        except Exception as e:
            print(e)
            return False
    
    def del_s_g(self, gpname):
        sql = 'delete from s_g_u_relation where s_g_u_id = %s'
        if not self.get_s_g_id(gpname):
            print('No relations of %s in s_g_u_relation table.' %gpname)
        else:
            s_g_id_list = self.get_s_g_id(gpname)
            try:
                for i in s_g_id_list:
                    params = i
                    self.__helper.delete(sql,params)
            except Exception as e:
                print(e)  
    
    def del_s_u(self, username):
        sql = 'delete from s_g_u_relation where s_g_u_id = %s'
        if not self.get_s_u_id(username):
            print('No relations of %s in s_g_u_relation table.' %username)
        else:
            s_u_id_list = self.get_s_u_id(username)
            try:
                for i in s_u_id_list:
                    params = i
                    self.__helper.delete(sql,params)
            except Exception as e:
                print(e)           

    def del_s_g_u(self, serip):
        sql = 'delete from s_g_u_relation where s_g_u_id = %s'
        if not self.get_s_u_g_id(serip):
            print('No relations of %s in s_g_u_relation table.' %serip)
        else:
            s_g_u_id_list = self.get_s_u_g_id(serip)
            try:
                for i in s_g_u_id_list:
                    params = i
                    self.__helper.delete(sql,params)
            except Exception as e:
                print(e)


'''
t = s_g_u_relation()
#t.add_s_g('192.168.0.1', 'gp2')
print(t.add_s_u('192.168.0.2', 'user1'))
'''



