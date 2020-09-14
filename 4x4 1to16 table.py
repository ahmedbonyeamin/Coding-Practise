# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 20:50:48 2020

@author: USER
"""


def table():
    t = []
    for j in range(4):
        row = []
        for i in range(1, 5):
            row += [i+(4*j)]
        t.append(row)
    return t

print(table())



"""n × n, and contains the numbers 1 to n^2"""
def table(n):
    t = []
    for j in range(n):
        row = []
        for i in range(1, n+1):
            row += [i+(n*j)]
        t.append(row)
    return t

print(table(5))

