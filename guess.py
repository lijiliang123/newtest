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
