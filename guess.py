import random
import pickle

numCount = 0  #计数器变量初始化
sjList = []   #列表对象声明


while numCount <= 9:
    sjsh = random.randint(0, 100)     #randint(a,b)产生的随机数包括上下临界值
    sjList.append(sjsh)               #列表对象append方法，往列表中增加item
    numCount += 1                     #计数器变量赋值

for i in range(len(sjList)):          #读出列表对象中的item
    print('第', i+1, '个数：', end='')
    print(sjList[i])

    wjnr = '第' + str(i+1) + '个数=' + str(sjList[i]) + '\n'
    with open('随机数', 'ab') as f:
        #pickle.dump(sjList[i], f)
        pickle.dump(wjnr, f)

with open('随机数', 'rb') as f:
    shch = pickle.load(f)
    if len(shch) > 0:
        print(shch, '\n')

"""
number=70
guess=int(input('Please input any number:'))

if guess==number:
    print('祝贺您，你猜对了.')
    print('但是没有任何奖品哦！')
elif guess<number:
    print('正确答案比这个数大一点，请继续玩游戏！')
else:
    print("正确答案要比这个数小一些，请继续玩游戏！")
print('结束')
"""
