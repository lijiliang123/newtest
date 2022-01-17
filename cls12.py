import random


class Student:
    # 类变量，定义在方法体之外，引用方法：类名.类变量名
    number = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        # 类里面的私有属性和私有方法以双下划线__开头。私有属性或方法不能在类的外部被使用或直接访问。
        self.__dscore = score * 2
        # 类变量引用，统计对象初始化次数
        Student.number = Student.number + 1

    def show(self):
        print("name:{}, score:{}".format(self.name, self.score))

    # 定义类方法时，前面需要用到修饰符@classmethod
    @classmethod
    # 类方法，参数固定为cls
    def total(cls):
        print("instance number:{0}".format(cls.number))

    # 定义静态方法，前面需要用到修饰符@staticmethod
    @staticmethod
    # 静态方法定义，既无self参数，也无cls参数
    def say():
        print("我是一个静态方法！既无self参数，也无cls参数！")

    # @property装饰器，将私有属性通过函数的方式伪装成对象可直接访问的公有属性
    @property
    def dscore(self):
        print("name:{}, double score:{}".format(self.name, self.__dscore))


# 定义match数据字典结构，用于将数字，转化为对应的中文大写
match = {1: "一",
         2: "二",
         3: "三",
         4: "四",
         5: "五",
         6: "六",
         7: "七",
         8: "八",
         9: "九",
         10: "十"}

times = 10
while times >= 1:
    stu = "stu" + str(times)
    # 数据字典结构，用[key]直接访问,取出value后与前一个字符串拼接
    stu = Student("张" + match[times], random.randint(10, 100))
    print(stu.show())
    # property装饰器伪装后的私有变量，以属性形式直接引用
    print(stu.dscore)
    times = times - 1
    continue

# 类方法调用：类名.方法名
Student.total()
# 静态方法调用：类名.方法名，或对象名.方法名
Student.say()


# 定义子类，从父类继续属性（name, score），并增加新的属性age
class SubStudent(Student):

    def __init__(self, name, score, age):
        # 调用父类进行继承属性的初始化
        Student.__init__(self, name, score)
        self.age = age
        print("子类正在初始化...哦...请稍候...")

    # 重写父类的show方法,增加输出age属性的值
    # 加双下划线后，__show方法，为私有方法，外部对象不能直接访问
    def __show(self):
        Student.show(self)
        print("age:{}".format(self.age))

    # 将私有方法包装成通用方法，供对象实例调用
    def reshow(self):
        # 类内部通过：类名.私有方法名（self），调用类的私有方法
        SubStudent.__show(self)


substu1 = SubStudent("儿子", 90, 18)
# substu1.show()
substu1.reshow()
