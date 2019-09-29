# -*- coding: utf-8 -*-
# @Time    : 2019/9/29 21:07
# @Author  : ty
# @File    : double_link_list.py

from single_list_change import *


class DLNode(LNode):
    """双链表结点类"""

    def __init__(self, elem, prev=None, next_=None):
        LNode.__init__(self, elem, next_)
        self.prev = prev


class DLList(LList1):
    """双链表"""

    def __init__(self):
        LList1.__init__(self)

    def prepend(self, elem):
        """前端插入"""
        p = DLNode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self, elem):
        """尾端插入"""
        p = DLNode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        """首端删除"""
        if self._head is None:
            raise LinkedListUnderflow("in pop_last of DLList")
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        """尾部删除"""
        if self._head is None:
            raise LinkedListUnderflow("in pop_last of DLList")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e
