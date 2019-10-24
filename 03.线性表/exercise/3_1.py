# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 10:39
# @Author  : ty
# @File    : single_link_list.py

# ADTList: #一个表抽象数据类型
# List(self) #表构造操作，创建一个新表
# isempty(self) #判断self是否为一个空表
# len(self) #获得selfW长度
# prepend(self， elem) #将元素elem加人表中作为第一个元素
# append(self, elem)将元素elem加人表中作为最后一个元素
# insert(self, elem, i) #将6^111加入表中作为第i个元素，其他元素的顺序不变
# del_first(self) #删除表中的首元素
# dellast(self) ^删除表中的尾元素
# search(self, elem) #查找元素  elem在表中出现的位置，不出现时返回-1
# forall(self, op)  #对表中的每个元素执行操作op


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
        self._num = 0

    def length(self):
        """长度"""
        count = 0
        cur = self._head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def is_empty(self):
        """判断表是否为空"""
        return self._head is None

    def prepend(self, elem):
        """表头插入数据"""
        self._head = LNode(elem, self._head)
        self._num += 1

    def pop(self):
        """删除表头结点"""
        if self._head is None:
            raise LinkedListUnderflow
        e = self._head.elem
        self._head = self._head.next
        self._num -= 1
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
        self._num += 1

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
        self._num -= 1
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

    def __len__(self):
        return self._num

    def insert(self, elem, i):
        """在位置i处插入元素elem"""
        if i == 0:
            self.prepend(elem)
        elif i == len(self) - 1:
            self.append(elem)
        elif i > 0 and i < len(self) - 1:
            p = self._head
            count = 0
            while count < i - 1:
                p = p.next
                count += 1
            node = LNode(elem)
            node.next = p.next
            p.next = node
        else:
            pass
        self._num += 1

    def search(self, e):
        i = 0
        p = self._head
        while p is not None:
            if p.elem == e:
                return i
            i += 1
            p = p.next
        return -1

    def forall(self, op):
        p = self._head
        while p is not None:
            op(p.elem)

    def delete(self, i):
        """给定位置的删除"""

        p = self._head
        if i == 0:
            self.pop()
        elif i == len(self) - 1:
            self.pop_lst()
        else:
            count = 0
            while count < i - 1:
                p = p.next
                count += 1
            p.next = p.next.next

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        pre = self._head
        aft = other._head
        while pre is not None:
            if pre.elem != aft.elem:
                print(pre.elem, aft.elem)
                return False
            pre = pre.next
            aft = aft.next
        return True

    @staticmethod
    def to_link(lst):
        """顺序表转换为链接表"""
        link = LList()
        for i in lst:
            link.prepend(i)
        return link

    def to_order(self):
        """链接表转换为顺序表"""
        lst = list()
        p = self._head
        while p is not None:
            lst.insert(0, p.elem)
            p = p.next
        return lst


if __name__ == '__main__':
    mlist1 = LList()
    mlist2 = LList()
    mlist3 = LList()
    for i in range(10):
        mlist1.prepend(i)
        mlist3.prepend(i)
    for i in range(11, 20):
        mlist2.append(i)
    ls = [1, 2, 3]
    # mlist1.insert(33, 3)
    # print(len(mlist1))
    # print(mlist1.length())
    # mlist1.printall()
    # print('*' * 50)
    # print(mlist1.search(55))
    # mlist1.delete(4)
    # mlist1.printall()
    # print("\n")
    # print(mlist1 == mlist2)
    # print(mlist1 == mlist3)
    # mlist1.for_each(print)
    # for x in mlist1.elements():
    #     print(x)
    ls = mlist3.to_order()
    print(type(ls))
    print(ls)
    link = LList.to_link(ls)
    print(type(link))

