#!/usr/bin/env python
#coding:UTF-8

from ebank.ui.ui import ui
from ebank.model.account import account

def login():
    while True:
        ui_handle = ui()
        account_handle = account()
        ui_handle.welcome()
        user = ui_handle.login()
        user_id = user[0]
        user_pwd = user[1]
        if not account_handle.chkUser(user_id):
            break
        elif not account_handle.chkPwd(user_id, user_pwd):
            break
        else:
            return ui_handle.serviceList()

def query(user_id):
    





def main():
    
    ser_id = login()
    print(ser_id)
    
    
            

if __name__ == '__main__':
    main()








