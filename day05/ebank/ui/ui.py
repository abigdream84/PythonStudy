#!/usr/bin/env python
#coding:UTF-8


class ui():
    
    def __init__(self):
        pass
    
    def welcome(self):
        print('********************************************************')
        print('*                                                      *')
        print('*             Welcome to our ebank!                    *')
        print('*                                                      *')
        print('********************************************************')

    def login(self):
        login_list = []
        user = input('Pleast input your username:')
        login_list.append(user)
        passwd = input('Please input your password:')
        login_list.append(passwd)
        return login_list

    def serviceList(self):
        print('                                                        ')
        print('                [1] Draw Money                          ')
        print('                [2] Query                               ')
        print('                [3] Deposit                              ')
        print('                [4] Transfer                            ')
        print('                [5] Quit                                ')
        print('                                                        ')
        choice = input('  Please choose the service:                    ')
        return choice


'''
ui = ui()
ui.login()
ui.serviceList()
'''

