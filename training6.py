"""
Python中的三种方法：
1. 实例方法，通过参数self引用
2. 类方法，通过参数cls引用，实际应用中可以通过：类名.类方法，或实例名.类方法，调用
3. 静态方法，不能用self，也不能用cls， 实际应用中可以通过：类名.静态方法，或实例名.静态方法，调用

"""


class Kls(object):
    def foo(self, x):  #实例方法，第一个参数self
        print('executing foo(%s,%s)' % (self, x))

    @classmethod  #类方法，第一个参数cls
    def class_foo(cls, x):
        print('executing class_foo(%s,%s)' % (cls, x))

    @staticmethod  ##静态方法，不能用参数self，也不能用cls，是一个放在类空间的独立函数
    def static_foo(x):
        print('executing static_foo(%s)' % x)


ik = Kls()  #类的实例化

# 实例方法
ik.foo(1)
print(ik.foo)  #打印方法属性
print('==========================================')

# 类方法
ik.class_foo(1)  #通过实例（也就是对象）访问类方法
Kls.class_foo(1)  #通过类名访问类方法
print(ik.class_foo)  #打印方法属性
print('==========================================')

# 静态方法
ik.static_foo(1)  #通过实例（也就是对象）访问静态方法
Kls.static_foo('hi')  #通过类名访问静态方法
print(ik.static_foo)  #打印方法属性

"""
上述程序输出结果：
executing foo(<__main__.Kls object at 0x0000018C2A4696C8>,1)
<bound method Kls.foo of <__main__.Kls object at 0x0000018C2A4696C8>>
***分析：从输出结果可以看出，实例方法在调用时，与实例（也就是对象）绑定
==========================================
executing class_foo(<class '__main__.Kls'>,1)
executing class_foo(<class '__main__.Kls'>,1)
<bound method Kls.class_foo of <class '__main__.Kls'>>
***分析：从输出结果可以看出，类方法在调用时，与类绑定
==========================================
executing static_foo(1)
executing static_foo(hi)
<function Kls.static_foo at 0x0000018C2A4488B8>
***分析：从输出结果可以看出，静态方法在调用时，既没有与实例（也就是对象）绑定，也没有与类绑定

"""
