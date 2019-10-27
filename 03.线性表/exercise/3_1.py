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

# -----------------------------------------------------------------------------------------------------
# 1. 检査本章开始定义的线性表抽象数据类型和3.3节定义的链表类LList,给LList加人在 抽象数
# 据类型中有定义，但LList类没定义的所有操作。
# 2. 请为LList类增加定位（给定顺序位置的）插入和删除操作。
# 3. 给LList增加一个元素计数值域mm,并修改类中操作，维护这个计数值。另外定义一个 求表中
# 元素个数的len函数。 Python的内置标准函数len可以自动调用用户定义类里的相 关函数_len_，
# 也可以用它作为方法名。请比较这种实现和原来没有元素计数值域的实 现，说明两者各自的
# 优缺点。
# 4. 请基于元素相等操作“=”定义一个单链表的相等比较函数。另请基于字典序的概念，为 链接
# 表定义大于、小于、大于等于和小于等于判断。
# 5. 请为链接表定义一个方法，它基于一个顺序表参数构造一个链接表；另请定义一个函数，它 从
# 一个链接表构造出一个顺序表。
# 6. 请为单链表类增加一个反向遍历方法rev_visit (self, op)， 它能按从后向前的顺序把 操作op
# 逐个作用于表中元素。你定义的方法在整个遍历中访问结点的总次数与表长度《是 什么关系？
# 如果不是线性关系，请设法修改实现，使之达到线性关系。这里要求遍历方法 的空间代价是
# 0(1)。（提示：你可以考虑为了遍历而修改表的结构，只要能在遍历的最后将
# 表结构复原。 ）
# 7. 请为单链表类定义下面几个元素删除方法，并保持其他元素的相对顺序：
# a) del_minimal()删除当时链表中的最小兀素；
# b) del_if (pred)删除当前链表里所有满足谓词函数pred的元素； C)del_dupliCate()删除表
# 中所有重复出现的元素。也就是说，表中任何元素的第一次
# 出现保留不动，后续与之相等的元素都删除。
# 要求这些操作的复杂度均为〇(…，其中《为表长。
# 8. 请为单链表类定义一个变动方法interleaving (self, another),它把另一个单链表 another
# 的元素交错地加人本单链表。也就是说，结果单链表中的元素是其原有元素与单 链表anothe
# r中元素的一一交错的序列。如果某个表更长，其剩余元素应位于修改后的单 链表的最后。
# 9. 考虑实现单链表插人排序的另一个想法：插入排序也就是把要排序的元素一个个按序插入到
# 一个元素已经排好序的链表里，从空链表开始。请根据这个想法实现另一个完成单链表排 序
# 的插入排序函数。
# 10. 定义一个单链表剖分函数partition(lst, pred),其参数为单链表1st和谓词函数 pred,函数p
# artition返回一对单链表（一个序对)， 其中第一个单链表包含着原链表 1st里所有值满足pr
# ed的结点，第二个链表里是所有其他结点。注意，两个表里的结点 还应保持原表里结点的相
# 对顺序。也就是说，如果在某结果表里结点a的后继结点是b， 在原表1st里a —定位于b之前。
# -----------------------------------------------------------------------------------------------------


def djuge_ord(num):
    if num % 2 == 0:
        return True
    return False


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
        """链表长度"""
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
        """查找元素"""
        i = 0
        p = self._head
        while p is not None:
            if p.elem == e:
                return i
            i += 1
            p = p.next
        return -1

    def forall(self, op):
        """正序遍历操作"""
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
        """判断两个链表是否相等"""
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

    def rev_visit(self, op):
        """倒序遍历操作"""
        link_1 = LList()
        p = self._head
        while p is not None:
            last = self.pop_lst()
            op(last)
            link_1.prepend(last)

    def del_minimal(self):
        """删除链表中的最小元素"""
        if self._head is None or self._head.next is None:
            return self._head
        cursor = self._head
        current_minimum = self._head.elem
        while cursor is not None:
            if current_minimum > cursor.elem:
                current_minimum = cursor.elem
            cursor = cursor.next

        cursor = self._head
        while cursor.next is not None:
            if cursor.next.elem == current_minimum:
                if cursor.next.next is None:
                    cursor.next = None
                else:
                    cursor.next = cursor.next.next
                break
            cursor = cursor.next

    def remove(self, value):
        """Removes value from the list or raises ValueError."""
        previous_node, matched_node = self._find_value(value)
        previous_node.next = matched_node.next

    def _find_value(self, value):
        previous, current = self._head, self._head.next

        while current is not None:
            if current.elem == value:
                return previous, current

            previous, current = current, current.next

        raise ValueError(f'value not in list')

    def del_if(self, pred):
        """删除当前链表里所有满足谓词函数pred的元素"""
        p = self._head
        while p:
            pred(p.elem)
            if pred(p.elem):
                self.remove(p.elem)
            p = p.next

    def del_duplicate(self):
        """删除表中所有重复出现的元素，复杂度为O(n2)"""
        current = second = self._head
        while current:
            while second.next:
                if second.next.elem == current.elem:
                    second.next = second.next.next
                else:
                    second = second.next
            current = second = current.next

    def intervleaving(self, another):
        """交错插入单链表"""
        re_link = LList()
        pre = self._head
        aft = another._head
        while (pre or aft):
            if pre:
                re_link.append(pre.elem)
                pre = pre.next
            if aft:
                re_link.append(aft.elem)
                aft = aft.next
        return re_link

    def insert_sort(self):
        """插入排序算法"""
        # sorted_linklist = LList()
        # sorted_linklist._head = self._head
        # current = self._head.next
        # s_current = self._head
        # while current:
        #     while s_current:
        #         if current.elem < s_current.elem:
        #             s_current.
        pass


if __name__ == '__main__':
    mlist1 = LList()
    mlist2 = LList()
    mlist3 = LList()
    for i in range(10):
        mlist1.prepend(i)
        # mlist3.prepend(i)
    for i in range(5, 10):
        mlist2.append(i)
    mlist1.printall()
    # mlist1.del_if(djuge_ord)
    # mlist1.del_duplicate()
    print('\n')
    re_linklist = mlist2.intervleaving(mlist1)
    re_linklist.printall()
    # ls = [1, 2, 3]
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
    # ls = mlist3.to_order()
    # print(type(ls))
    # print(ls)
    # link = LList.to_link(ls)
    # print(type(link))
