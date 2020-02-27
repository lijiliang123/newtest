#打印九九乘法表
def jjcfb():
    hang = 0
    lie = 0

    for lie in range(1, 10):
        s1 = '现在打印 ' + str(lie)+' 的乘法口诀'
        print('{0:*^16}'.format(s1))
        #print('*' * 20)
        #print('现在打印', lie, '的乘法口诀')
        #print('*' * 20)

        for hang in range(lie, 10):
            print(lie, '*', hang, '=', lie*hang)

        if lie == 9:
            print('{0:*^20}'.format('九九乘法表打印结束'))


jjcfb()

print('函数调用成功！')
