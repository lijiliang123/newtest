#方式一：通过【for】方法实现
for i in range(1, 10):
    for j in range(1, i+1):
        d = i * j
        print('%d*%d=%-3d' % (i, j, d), end=' ')
        #字符串输出说明：%后面，d代表输出类型为整型，-代表左对齐，3代表输出宽度为3个字符
    print()

print('下面用另一种实现方法：while 实现')

#方式二：通过【while】方法实现
i = 1
while i < 10:
    j = 1
    while j <= i:
        print("%d*%d=%2d" % (j, i, j*i), end=' ')
        j += 1
    print("")
    i += 1
