#函数定义:
def game():

    running = True
    while running:

        n1 = int(input('请输入第一个数字：'))
        n2 = int(input('请输入第二个数字：'))
        if n1 > n2:

            print(n1, '大于', n2)
        elif n1 == n2:
            print(n1, '等于', n2)
            running = False
        else:
            print(n1, '小于', n2)
    else:
        print('游戏结束了！')

#以下为全局变量：


_version_ = 0.3
_name_ = 'dddretr'
_adrress_ = '广州'
_author_ = 'Thomae Lee'

#函数调用:
game()

'''
  Python语言，一定要注意程序块的缩进格式，否则代码对，执行结果也不一定对哦！
  切记，切记！

'''


