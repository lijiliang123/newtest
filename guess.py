import random

numCount = 0
sjList = []
while numCount <= 9:
    sjsh = random.randint(0, 10)
    sjList.append(sjsh)
    numCount += 1
for i in range(len(sjList)):
    print('第', i+1, '个数：', end='')
    print(sjList[i])




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
