import random


class MyFormula:

    # 类初始化方法 __init__(self)
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print('The class object is initializing:{},{},{}'.format(self.a, self.b, self.c))

    @classmethod
    # 类方法，第1个参数固定为cls
    def jdz(cls, n):
        print('Now, it is running absolute function... ')
        if n >= 0:
            return n
        else:
            return n * (-1)

    @classmethod
    # 类方法，第1个参数固定为cls
    def area(cls, a, b):
        print('Now, it is running area function...')
        return a * b


# 类对象初始化
mynum = MyFormula(0, 0, 0)

num = int(input('Pls input any number: '))
print('The number absolute value is: ', mynum.jdz(num))

lgh = int(input('Pls input the length: '))
wdt = int(input('Pls input the width: '))
print('The area is:', mynum.area(lgh, wdt), '平方米')
