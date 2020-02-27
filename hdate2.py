import random
a=round(random.random(),6) #生成一个0～1的随机数，可以指定小数位数
b=format(100,'b') #转换为二进制输出
print(a)
print(b)

#下面是一个显示当前日期、星期几的一个小程序
from datetime import datetime, timedelta
#XingQi(ind)函数，将weekday()返回的值0~6，转换成中文的星期几
def XingQi(ind):
    if ind==0:
        return '一'
    elif ind==1:
        return '二'
    elif ind==2:
        return '三'
    elif ind==3:
        return '四'
    elif ind==4:
        return '五'
    elif ind==5:
        return '六'
    elif ind==6:
        return '日'

def JinRi():
    now=datetime.today()
    nian=now.year
    yue=now.month
    riqi=now.day
    xq=XingQi(now.weekday())
    s1='今天是：'
    s2='年'
    s3='月'
    s4='日'
    s5='星期'
    print(s1,nian,s2,yue,s3,riqi,s4,s5,xq)

JinRi()  #函数调用

day1=datetime(2018,10,2)
day2=day1+timedelta(days=10)  #计算多少天之后，使用timedelta方法
print(day2)

#以下程序输出当前月的日期范围
from datetime import datetime, date, timedelta
import calendar
def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
        _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
        end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)

a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day

dt1=datetime.today()
dt2=date.today()


print(dt1)
print(dt2)

ll=[1,2,3,4]
for i in ll:
    print(i,end=' ')


