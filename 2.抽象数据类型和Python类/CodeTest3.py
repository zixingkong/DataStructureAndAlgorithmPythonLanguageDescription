# -*- coding: utf-8 -*-
# @Time    : 2019/9/24 21:43
# @Author  : ty
# @File    : CodeTest3.py
# 3. 扩充本章给出的有理数类，加人一些功能：
# a) 其他运算符的定义；
# b) 各种比较和判断运算符的定义；
# c) 转换到整数（取整） 和浮点数的方法；
# d) 给初始化函数加人从浮点数构造有理数的功能（Python标准库浮点数类型的as_ integer_
# ratio()函数可以用在这里）〇抽象数据类型和Python类 65
# 对应运算符的特殊函数名请查看语言手册3.3.7节（Emulating numeric types)。
class Rational():
    @staticmethod
    def _gcd(m, n):
        """求两个整数的最大公约数"""
        if n == 0:
            m, n = n, m

        while m != 0:
            m, n = n % m, m
        return n

    def __new__(cls, num, den):
        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        return super(Rational, cls).__new__(cls)

    def __init__(self, num, den=1):

        # if isinstance(num, float):
        #     num, den = num.as_integer_ratio()

        if not isinstance(num, int) or not isinstance(den, int):
            raise TypeError
        if den == 0:
            raise ZeroDivisionError
        sign = 1

        if num < 0:
            num, sign = -num, -sign
        if den < 0:
            den, sign = -den, -sign

        g = Rational._gcd(num, den)
        self._num = sign * (num // g)
        self._den = den // g
        print(self._num)
        print(self._den)

    def num(self):
        return self._num

    def den(self):
        return self._den

    def __add__(self, other):
        den = self._den * other.den()
        num = (self._num * other.den() +
               self._den * other.num())
        return Rational(num, den)

    def __sub__(self, other):
        return Rational(self._num * other.den() - self._den * other.num(),
                        self._den * other.den())

    def __mul__(self, other):
        return Rational(self._num * other.num(),
                        self._den * other.den())

    def __floordiv__(self, other):
        """定义整数除法的行为：//"""
        if other.num() == 0:
            raise ZeroDivisionError
        return Rational(self._num * other.den(),
                        self._den * other.num())

    # TODO
    def __truediv__(self, other):
        """定义真除法的行为：/"""
        if other.num() == 0:
            raise ZeroDivisionError
        return Rational(self._num * other.den(),
                        self._den * other.num())

    # TODO
    def __mod__(self, other):
        pass

    def __eq__(self, other):
        return self._num * other.den() == self._den * other.num()

    def __lt__(self, other):
        return self._num * other.den() < self._den * other.num()

    #
    def __ne__(self, other):
        return self._num * other.den() != self._den * other.num()

    #
    def __le__(self, other):
        return self._num * other.den() <= self._den * other.num()

    #
    def __gt__(self, other):
        return self._num * other.den() > self._den * other.num()

    #
    def __ge__(self, other):
        return self._num * other.den() >= self._den * other.num()

    def __str__(self):
        return str(self._num) + "/" + str(self._den)

    def print(self):
        print(self._num, "/", self._den)

    def get_int(self):
        return int(self._num / self._den)

    def get_float(self):
        return self._num / self._den


if __name__ == "__main__":
    r1 = Rational(2, 3)
    print(r1.num())
