def compare(n1, n2):  #带参数的函数定义
    if n1 == n2:
        print(n1, '等于', n2)
    elif n1 > n2:
        print(n1, '大于', n2)
    else:
        print(n1, '小于', n2)
#函数 compare(n1,n2) 结束


def say(message, times=1):
    print(message * times)


def cal():        #不带参数的函数定义
    a = int(input('请输入一个数字：'))
    b = int(input('请输入另一个数字：'))
    compare(a, b)  #调用函数 compare(n1,n2)
    summ = a+b
    mul = a*b
    print('这两个数字之和为：', summ)
    print('这两个数字之积为：', mul)
    print('这是我的第一个python函数,还包含了另一个函数的调用。')
    say('hello')        #调用函数say()
    say('hello ', 5)     #调用函数say()


cal()     #调用函数cal()


print('{0:*^20}'.format('函数调用结束！'))


