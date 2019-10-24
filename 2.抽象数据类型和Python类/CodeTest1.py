# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 20:35
# @Author  : ty
# @File    : CodeTest.py
# 编程练习
# 1. 定义一个表示时间的类Time,它提供下面操作：
# a) Time (hours、 minutes、 seconds)创建一个时间对象；
# b) t.hours ()、 t.minutes ()、 t.seconds ()分别返回时间对象t的小时、分钟和秒值；
# c) 为Time对象定义加法和减法操作（用运算符+和-)；
# d) 定义时间对象的等于和小于关系运算（用运算符=和<)。
# 注意： Time类的对象可以采用不同的内部表示方式。例如，可以给每个对象定义三 个数
# 据属性hours、 minutes和seconds,基于这种表示实现操作。也可以用一个属性 seconds,构造对
# 象时算出参数相对于基准时间〇点〇分〇秒的秒值，同样可以实现所有 操作。请从各方面权
# 衡利弊，选择合适的设计。
# 上面情况表现出“抽象数据类型”的抽象性，其内部实现与使用良好隔离，换一种实 现
# 方式（或改变一些操作的实现技术）可以不影响使用它的代码。

class Time():
    def __init__(self, hours, minutes, seconds):
        if not (isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int)):
            raise TypeError
        if (0 <= hours <= 23):
            self._hours = hours
            if (0 <= minutes <= 59):
                self._minutes = minutes
                if (0 <= seconds <= 59):
                    self._seconds = seconds
                else:
                    raise ValueError("%d is not valid seconds" % seconds)
            else:
                raise ValueError("%d is not valid minutes" % minutes)
        else:
            raise ValueError("%d is not valid hours" % hours)

    def hours(self):
        return self._hours

    def minutes(self):
        return self._minutes

    def seconds(self):
        return self._seconds

    def __add__(self, other):  # 定义加法行为
        seconds_add = self._seconds + other._seconds
        seconds_carry = seconds_add // 60
        seconds = seconds_add % 60
        minutes_add = self._minutes + other._minutes + seconds_carry
        minutes_carry = minutes_add // 60
        minutes = minutes_add % 60
        hours_add = self._hours + other._hours + minutes_carry
        if hours_add < 24:
            hours = hours_add
        else:
            hours = hours_add - 24
        return Time(hours, minutes, seconds)

    def __sub__(self, other):  # 定义减法行为
        if self._seconds < other._seconds:
            self._minutes -= 1
            seconds = self._seconds + 60 - other._seconds
        else:
            seconds = self._seconds - other._seconds
        if self._minutes < other._minutes:
            self._hours -= 1
            minutes = self._minutes + 60 - other._minutes
        else:
            minutes = self._minutes - other._minutes
        if self._hours < other._hours:
            hours = self._hours + 24 - other._hours
        else:
            hours = self._hours - other._hours
        return Time(hours, minutes, seconds)

    def __eq__(self, other):  # 定义等于号行为
        boolean1 = False
        boolean2 = False
        boolean3 = False
        if self._hours == other._hours:
            boolean1 = True

        if self._minutes == other._minutes:
            boolean2 = True
        if self._seconds == other._seconds:
            boolean3 = True
        return boolean1 and boolean2 and boolean3

    def __lt__(self, other):  # 定义小于号行为
        if self._hours < other._hours:
            return True
        elif self._hours == other._hours:
            if self._minutes < other._minutes:
                return True
            elif self._minutes == other._minutes:
                if self._seconds < other._seconds:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def print(self):
        print(self._hours + ':' + self._minutes + ':' + self._seconds)

    def __str__(self):
        return str(self._hours) + ':' + str(self._minutes) + ':' + str(self._seconds)


# 4. 本章2.2.2节中有理数类的实现有一个缺点：每次调__init_都会对两个参数做一遍彻底 检查。
# 但是，在有理数运算函数中构造结果时，其中一些检查并不必要，浪费了时间。请 查阅Pyth
# on手册中与类有关的机制，特别是名字为_new_的特殊方法等，修改有关设计， 使得到的实现
# 能完成工作但又能避免不必要的检查。
# 5.请基于2.5节的工作继续扩充，为该学校人事系统定义研究生类、教师类和职员类。


if __name__ == '__main__':
    t = Time(21, 31, 59)
    t1 = Time(18, 31, 41)
    he = t + t1
    cha = t - t1
    print(he)
    print(cha)
    print(t == t1)
    print(t < t1)
    print(he.hours())
