#!/usr/bin/env python
#coding:UTF-8

from example.model.test import test

def main():
    testTable = test()
    testTable.deleteId(('id',10))


if __name__ == '__main__':
    main()
    





