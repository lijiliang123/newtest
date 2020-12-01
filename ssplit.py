import random
'''
for i in range(10):
    n1 = random.randint(0, 10)
    print(n1, end=' ')
    print('@' * n1)  #输出
'''

#打印九九乘法表

hang = 0
lie = 0

for lie in range(1, 10):
    print('*' * 20, end='')
    print('现在打印', lie, '的乘法口诀', end='')
    print('*' * 20)

    for hang in range(lie, 10):
        print(lie, '*', hang, '=', lie*hang)

    if lie == 9:
        print('*' * 20)
        print('乘法表打印结束')
        print('*' * 20)




