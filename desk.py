import time

# 获取当前时间中的小时数
curhour = int(time.localtime().tm_hour)


# 变量名与方法名，一定不能重复～


def move():
    print('桌子被移动！')


class desk:
    def __init__(self, longth, width, height):
        self.longth = longth
        self.width = width
        self.height = height
        print('桌子正在初始化过程中......')
        print('长度{}米、宽度{}米、高度{}米'.format(self.longth, self.width, self.height))
        print('桌子初始化完毕！')

    def knock(self):
        print('桌子被敲打！')


class dinnerDesk(desk):

    def __init__(self, longth, width, height, breakfast, lunch, dinner):
        desk.__init__(self, longth, width, height)
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
        print('饭桌正在初始化过程中......')
        print('早餐时间是：{}点钟'.format(self.breakfast))
        print('晚餐时间是：{}点钟'.format(self.dinner))
        print('午餐时间是：{}点钟'.format(self.lunch))
        print('饭桌初始化结束！')
        print('*'*20)

    def morning(self):
        if curhour == self.breakfast:
            print('{}点钟早餐时间到，开始吃早餐！'.format(self.breakfast))
        # print('{}点钟早餐时间到，开始吃早餐！'.format(self.breakfast))

        # print('{}点钟早餐时间到，开始吃早餐！'.format(self.breakfast))

    def noon(self):
        if curhour == self.lunch:
            print('{}点钟午餐时间到，开始吃午餐！'.format(self.lunch))

    # print('{}点钟午餐时间到，开始吃午餐！'.format(self.lunch))

    def evening(self):
        if curhour == self.dinner:
            print('{}点钟晚餐时间到，开始吃晚餐！'.format(self.dinner))

    # print('{}点钟晚餐时间到，开始吃晚餐！'.format(self.dinner))

    def adb(self):
        if curhour == self.dinner:
            print('ddd')
        elif curhour == self.dinner:
            print('deedd')
        else:
            print('ddffd')


my = dinnerDesk(2, 3, 4, 7, 12, 16)
move()
my.knock()
my.morning()
my.noon()
my.evening()

hh = int(time.localtime().tm_hour)
mm = int(time.localtime().tm_min)
ss = int(time.localtime().tm_sec)
print(hh, ':', mm, ':', ss)
# print(time.asctime())

print('今天的日期是:', time.strftime('%Y-%m-%d', time.localtime()))
print('当前时间是:', time.strftime('%H:%M:%S', time.localtime()))
print(time.strftime('%Y/%m/%d', time.localtime()))
