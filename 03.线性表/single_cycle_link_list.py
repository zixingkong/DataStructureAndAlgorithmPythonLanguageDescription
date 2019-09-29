# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 20:36
# @Author  : ty
# @File    : single_cycle_link_list.py


class LinkedListUnderflow(ValueError):
    pass


class LNode(object):
    def __init__(self, elem, next_=None):
        """表结点类"""
        self.elem = elem
        self.next = next_


class LCList():
    """循环单链表类"""

    def __init__(self):
        self._rear = None

    def is_empty(self):
        """判空"""
        return self._rear is None

    def prepend(self, elem):
        """前端插入"""
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        """尾端插入"""
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        """前端弹出"""
        if self._rear is None:
            return LinkedListUnderflow("in pop of CLList")
        p = self._rear.next
        if self._rear is p:
            self._rear = None
        else:
            self._rear.next = p.next

        return p.elem

    def printall(self):
        """输出表元素"""
        if self.is_empty():
            return
        p = self._rear.next
        while True:
            print(p.elem)
            if p is self._rear:
                break
            p = p.next
