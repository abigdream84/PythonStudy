#!/usr/bin/env python
#coding:UTF-8

def outter(fun):
    def wrapper(arg):
        print('before')
        result = fun(arg)
        print('after')
        return result
    return wrapper

@outter
def Fun1(arg):
    print('Fun1'+arg)
    return 'return111'

response = Fun1('haha')
print(response)



