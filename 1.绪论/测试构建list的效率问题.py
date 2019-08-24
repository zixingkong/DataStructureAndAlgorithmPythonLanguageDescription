# -*- coding: utf-8 -*-
# @Time    : 2019/8/24 20:36
# @Author  : ty
# @File    : 测试构建list的效率问题.py

from timeit import Timer


def t1(n):
    lst = []
    for i in range(n * 10000):
        lst = lst + [i]

    return lst


def t2(n):
    lst = []
    for i in range(n * 10000):
        lst.append(i)
    return lst


def t3(n):
    return [i for i in range(n * 10000)]


def t4(n):
    return list(range(n * 10000))


def t5(n):
    lst = []
    for i in range(n * 1000):
        lst += [i]
    return lst


def t6(n):
    lst = []
    for i in range(n * 1000):
        lst.insert(0, i)
    return lst


timer1 = Timer(stmt="t1(10)", setup="from __main__ import t1")
print("+ :", timer1.timeit(1))

timer5 = Timer(stmt="t5(10)", setup="from __main__ import t5")
print("+= :", timer5.timeit(1))

timer2 = Timer(stmt="t2(10)", setup="from __main__ import t2")
print("append :", timer2.timeit(1))

timer3 = Timer(stmt="t3(10)", setup="from __main__ import t3")
print("[i for i in range(n * 10000)] :", timer3.timeit(1))

timer4 = Timer(stmt="t4(10)", setup="from __main__ import t4")
print("list(range(n * 10000)) :", timer4.timeit(1))

timer6 = Timer(stmt="t6(10)", setup="from __main__ import t6")
print("lst.insert(0, i) :", timer6.timeit(1))
