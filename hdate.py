from decimal import Decimal
from decimal import localcontext

n1=Decimal('1.245')
n2=Decimal('2.8992')
print(n1+n2)

# 通过上下文设置输出精度
with localcontext() as ctx:
    ctx.prec=20   #设置运算结果的精度
    print(n1/n2)

# 格式化输出
n3=10
print(format(n3,'b'))  #将数字转化为二进制输出
print(format(n3,'o'))  #将数字转化为八进制输出
print(format(n3,'x'))  #将数字转化为十六进制输出

#numpy模块的使用，对列表、数组有强大的运算能力
import numpy as np
a=[1,2,3,4,5]
b=[6,7,8,9,10]
print(a+b)                #输出结果是两个列表的连接
print(sum(x for x in a))
print(sum(x*x for x in a))

ax=np.array([1,2,3,4,5])  #使用numpy构建数组
bx=np.array([6,7,8,9,10])
print(ax+bx)              #输出结果是两个列表的元素求和,条件是两个列表的元素个数必须相等
print(ax*2, bx*2, ax*bx)

import random
a1=[1,2,3,4,5]
print(random.choice(a1))  #随机输出指定列表中的元素
print(random.sample(a1,2)) #随机从指定列表中抽取特定数目的样本
print(random.randint(0,100)) #随机生成100内的整数
'''
 :一个猜数字小游戏
 ：利用random.randint()生成一个随机数
 ：玩游戏者通过提示最终猜到这个随机数
'''
import pickle
tips='''
Please select the game level:
1. Grade 1;
2. Grade 2;
3. Grade 3;
'''
#print(tips)
print('{0:*^150}'.format(tips))
grade=int(input('You select the Grade: '))
if grade==1:
    sjsh=random.randint(0,10)
elif grade==2:
    sjsh=random.randint(0,50)
else:
    sjsh=random.randint(0,100)

jx=True  #控制循环
cishu=0  #统计累计猜的次数
neirong={} #dic数据结构保存记录
#neirong.keys=input('Pls input your name: ')
#name=input('Pls input your name: ')
while jx:
    a=int(input('Pls input a number: '))
    if a==sjsh:
        cishu+=1
        print('Great!The suijishu is:',sjsh)
        print('You have guessed times:',cishu)
        with open('猜一猜.txt','ab') as f:  #open()参数a，追加写入文件
            neirong[input('Pls input your name: ')]=cishu
            #jilu=name+': '+str(cishu)
            pickle.dump(neirong,f)  #序列化写入文件
            #f.write(neirong)
        jx=False
    elif a<sjsh:
        print('Small!')
        cishu+=1
        continue
    else:
        print('Big!')
        cishu+=1
        continue

#print(format('猜数字排行榜','^50')
with open('猜一猜.txt','rb') as f:
    while True:
        try:
            line=pickle.load(f)  #反序列化输出文件
            print(line)
        except EOFError:
            break               #抛出异常时退出
        #line=f.readline()       #普通文件输出方式
        #if len(line)==0:
        #    break
        #else:
        #    print(line)



