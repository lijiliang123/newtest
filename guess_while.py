number=50
running=True

while running:
    guess=int(input('请随意输入一个数字：'))
    if guess==number:
        print('恭喜！您猜对了。')
        print('但没有奖品哦。')
        running=False
    elif guess<number:
        print('您输入的数字有点小哦，试下大的数字！')
    else:
        print('您输入的数字有点大哦，试下小的数字！')
else:  # 在python中，while循环的false处理
    print('循环结束！')


print('游戏结束')
