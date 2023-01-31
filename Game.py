"""
 :一个猜数字小游戏
 ：利用random.randint()生成一个随机数
 ：玩游戏者通过提示最终猜到这个随机数
"""
import random
import pickle
from datetime import datetime,date
tips = """
Please select the game level:
1. Grade 1;
2. Grade 2;
3. Grade 3;
"""
#print(tips)
print('{0:*^150}'.format(tips))
grade = int(input('You select the Grade: '))
if grade == 1:
    sjsh = random.randint(0, 10)
elif grade == 2:
    sjsh = random.randint(0, 50)
else:
    sjsh = random.randint(0, 100)

jx = True  #控制循环
cishu = 0  #统计累计猜的次数
neirong = {}  #dic数据结构保存记录
#neirong.keys=input('Pls input your name: ')
#name=input('Pls input your name: ')
while jx:
    a = int(input('Pls input a number: '))
    if a == sjsh:
        cishu += 1
        print('Great!The suijishu is:', sjsh)
        print('You have guessed times:', cishu)
        with open('猜一猜.txt', 'ab') as f:  #open()参数a，追加写入文件
            neirong[input('Pls input your name: ')] = cishu
            #jilu=name+': '+str(cishu)
            pickle.dump(neirong, f)  #序列化写入文件
            #f.write(neirong)
        jx = False
    elif a < sjsh:
        print('Small!')
        cishu += 1
        continue
    else:
        print('Big!')
        cishu += 1
        continue

#print(format('猜数字排行榜','^50')
with open('猜一猜.txt', 'rb') as f:
    while True:
        try:
            line = pickle.load(f)  #反序列化输出文件
            if len(line) >= 0:
                print(line)
            #print(line)
        except EOFError:
            break               #抛出异常时退出
        #line=f.readline()       #普通文件输出方式
        #if len(line)==0:
        #    break
        #else:
        #    print(line)

# amend on 2023-1-31 by thomas
