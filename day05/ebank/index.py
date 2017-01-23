#!/usr/bin/env python
#coding:UTF-8

from ebank.ui.ui import ui
from ebank.model.account import account
from ebank.model.balance import balance

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
            return user_id

def query(user_id):
    balance_handle = balance()
    user_balance = balance_handle.query(user_id)
    user_balance_tmp = str(user_balance)
    print("Your balance is:"+user_balance_tmp)

def drawMoney(user_id):
    balance_handle = balance()
    while True:
        amount = input('How much money do you want to draw:')
        flag = balance_handle.drawMoney(user_id, amount)
        if flag == 1:
            print('The amount you input is grater than your balance. Try again!')
            continue
        elif flag == 2:
            print('Please give a data!')
            continue
        else:
            print('Draw money successfully!')
            break
            
def depositMoney(user_id):
    balance_handle = balance()
    while True:
        amount = input('How much money do you want to deposit:')
        flag = balance_handle.depositMoney(user_id, amount)
        if flag == 0:
            print('Deposit money successfully!')
            break
        else:
            print('Please give a data!')
            continue

def transfer(user_id):
    balance_handle = balance()
    account_handle = account()
    while True:
        user_des = input('Which account do you want to transfer:')
        if not account_handle.chkUser(user_des):
            continue
        else:
            amount = input('How much money do you want to deposit:')
            flag = balance_handle.transfer(user_id, user_des, amount)
            if flag == 1:
                print('The amount you input is grater than your balance. Try again!')
                continue
            elif flag == 2:
                print('Please give a data!')
                continue
            else:
                print('Draw money successfully!')
                break


def main():
    ui_handle = ui()
    while True:
        user_id = login()
        if not user_id:
            continue
        else:
            while True:
                ser_id = ui_handle.serviceList()
        
                if ser_id == '1':
                    drawMoney(user_id)
                    yn_temp = ui_handle.y_or_n()
                    if yn_temp:
                        continue
                    elif not yn_temp:
                        exit()
                    else:
                        continue
                           
                if ser_id == '2':
                    query(user_id)
                    yn_temp = ui_handle.y_or_n()
                    if yn_temp:
                        continue
                    elif not yn_temp:
                        exit()
                    else:
                        continue
    
                if ser_id == '3':
                    depositMoney(user_id)
                    yn_temp = ui_handle.y_or_n()
                    if yn_temp:
                        continue
                    elif not yn_temp:
                        exit()
                    else:
                        continue
    
                if ser_id == '4':
                    transfer(user_id)
                    yn_temp = ui_handle.y_or_n()
                    if yn_temp:
                        continue
                    elif not yn_temp:
                        exit()
                    else:
                        continue

                elif ser_id == '5':
                    exit()
    
    
if __name__ == '__main__':
    main()








