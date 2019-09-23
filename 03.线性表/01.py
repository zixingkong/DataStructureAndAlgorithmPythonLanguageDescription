# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 22:23
# @Author  : ty
# @File    : 01.py

# 1. 检査本章开始定义的线性表抽象数据类型和3.3节定义的链表类LList,给LList加人在 抽象数
# 据类型中有定义，但LList类没定义的所有操作。

class LNode:
    def __init__(self, elem, next_=None):
        self.elem = elem
        self.next = next_


