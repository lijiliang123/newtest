import random

'''
Python中的方法，有三类：
1、成员方法，上面不用任何装饰器，直接使用def关键字，第1个参数必须是self
2、类方法，上面使用@classmethod装饰器修饰，第1个参数必须是cls
3、静态方法，上面使用@staticmethod装饰器修饰，无特定参数要求


'''


class MyFormula(object):

    # 类初始化方法 __init__(self)
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        print('The class object is initializing:{},{},{}'.format(self.a, self.b, self.c))

    # 成员方法
    def say(self):
        print('Hello, world!')

    # 类方法，第1个参数固定为cls
    @classmethod
    def jdz(cls, n):
        print('Now, it is running absolute function... ')
        if n >= 0:
            return n
        else:
            return n * (-1)

    # 类方法，第1个参数固定为cls
    @classmethod
    def area(cls, a, b):
        print('Now, it is running area function...')
        return a * b

    # 静态方法定义，既无self参数，也无cls参数
    @staticmethod
    def tj(a, b, c):
        print('Now, it is running tiji static function')
        return a * b * c


# 类对象初始化
mynum = MyFormula(0, 0, 0)

num = int(input('Pls input any number: '))
print('The number absolute value is: ', mynum.jdz(num))

lgh = int(input('Pls input the length: '))
wdt = int(input('Pls input the width: '))
print('The area is:', mynum.area(lgh, wdt), '平方米')

lgh = int(input('Pls input the length: '))
wdt = int(input('Pls input the width: '))
hgt = int(input('Pls input the height: '))
print('The 体积 is:', mynum.tj(lgh, wdt, hgt), '立方米')
