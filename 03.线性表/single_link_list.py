# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 10:39
# @Author  : ty
# @File    : single_link_list.py


class LinkedListUnderflow(ValueError):
    pass


class LNode(object):
    def __init__(self, elem, next_=None):
        """表结点类"""
        self.elem = elem
        self.next = next_


class LList():
    """单链表类"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断表是否为空"""
        return self._head is None

    def prepend(self, elem):
        """表头插入数据"""
        self._head = LNode(elem, self._head)

    def pop(self):
        """删除表头结点"""
        if self._head is None:
            raise LinkedListUnderflow
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, elem):
        """表尾插入节点"""
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(elem)

    def pop_lst(self):
        """删除表尾元素"""
        if self._head is None:
            raise LinkedListUnderflow("in pop_last")

        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e

        while p.next.next is not None:
            p = p.next

        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        """查询"""
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        """遍历打印表"""
        p = self._head
        while p is not None:
            print(p.elem, end='')
            if p.next is not None:
                print(', ', end="")
            p = p.next
        # print('')

    def for_each(self, proc):
        """遍历"""
        p = self._head
        while p is not None:
            proc(p.elem)
            p = p.next

    def elements(self):
        """生成器"""
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def filter(self, pred):
        """筛选生成器"""
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next


if __name__ == '__main__':
    mlist1 = LList()
    for i in range(10):
        mlist1.prepend(i)
    for i in range(11, 20):
        mlist1.append(i)

    mlist1.printall()
    print("=" * 50)
    # mlist1.for_each(print)
    for x in mlist1.elements():
        print(x)
