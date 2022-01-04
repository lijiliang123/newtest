import random


class Student:
    # 类变量，定义在方法体之外，引用方法：类名.类变量名
    number = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        # 类变量引用，统计对象初始化次数
        Student.number = Student.number + 1

    def show(self):
        print("name:{}, score:{}".format(self.name, self.score))

    # 定义类方法时，前面需要用到修饰符@classmethod
    @classmethod
    # 类方法，参数固定为cls
    def total(cls):
        print("instance number:{0}".format(Student.number))


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
    times = times - 1
    continue

# 类方法调用：类名.方法名
Student.total()
