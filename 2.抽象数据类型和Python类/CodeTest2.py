# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 21:37
# @Author  : ty
# @File    : CodeTest2.py
# 2. 请定义一个类，实现本章描述的Date抽象数据类型。


# class Date():
#     def __init__(self, year, mouth, day):
#         if not (isinstance(year, int) and isinstance(mouth, int) and isinstance(day, int)):
#             raise TypeError
#         if (year > 0):
#             self._year = year
#             if (0 <= mouth <= 12):
#                 self._mouth = mouth
#                 if (0 <= day <= 31):
#                     self._day = day
#                 else:
#                     raise ValueError("%d is not valid day" % day)
#             else:
#                 raise ValueError("%d is not valid mouth" % mouth)
#         else:
#             raise ValueError("%d is not valid year" % year)
#
#     def difference(self, other):
#         pass
#
#     def plus(self, d, t):
#         pass
#
#     def num_date(self, year, n):
#         pass
#
#     def ajust(selfd, n):
#         pass
"""

这里Date里简略的将每个月都视为30天，一年为360天

"""


class Date(object):

    def __init__(self, year=2018, month=10, day=5):
        self.year = year
        self.month = month
        self.day = day

        if self.year < 0:
            self.year = 0
            print("输入年份出错，年份请大于0年")
        if self.month < 1:
            self.month = 1
        elif self.month > 12:
            self.month = 12
            print("输入月份出错，月份请大于或等于1月，小于或等于12月")
        if self.day < 1:
            self.day = 1
        elif self.day > 30:
            self.day = 30
            print("输入日期出错，日期请大于或等于1号，小于或等于30号")

    def __str__(self):
        return "{}年{}月{}日".format(self.year, self.month, self.day)

    def difference(self, other):

        d1 = self.year * 360 + self.month * 30 + self.day
        d2 = other.year * 360 + other.month * 30 + other.day
        result = d1 - d2
        if result < 0:
            result = -1 * result
        return "两个日期差%d天" % result

    def plus(self, n):
        day, month, year = self.day, self.month, self.year
        day = day + n
        while day > 30:
            month = month + 1
            day -= 30

        while month > 12:
            year = year + 1
            month -= 12

        return "{}年{}月{}日".format(year, month, day)

    def num_date(self, year, n):
        year = self.year
        month = 1
        if n > 360 or n < 0:
            print("找不到这天，输入的天数有误")
        else:
            while n > 30:
                month += 1
                n -= 30
            if month > 12:
                return "范围出错，找不到这天"
        day = n
        return "{}的{}天是{}月{}日".format(year, n, month, day)

    def adjust(self, n):
        self.day += n
        if self.day > 0:
            while self.day > 30:
                self.day -= 30
                self.month += 1
            while self.month > 12:
                self.month -= 12
                self.year += 1
        else:
            while self.day < 0:
                self.day += 30
                self.month -= 1
            while self.month < 1:
                self.year -= 1
                self.month += 12
            if self.year < 0:
                return "调整日期出错，超出范围"

        return "{}年{}月{}日".format(self.year, self.month, self.day)
