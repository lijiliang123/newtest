"""
for i in range(1, 11):
    print('*' * i, )
    # print('*'*i, '(', i, ')')
"""
# 以下是打印出*形三角形的算法
# row, column,

columnList = []  # 存放每行输出的*数量
blankList = []   # 存放每行输出的空格数
normalList = []  # 过渡list, 存放过渡数据

rowCount = int(input('请输入您需要打印的三角形的行数: '))

# 求出每行输出的*的数量，并放入list中
for i in range(1, rowCount*2, 2):
    columnCount = i
    columnList.append(i)
    # print(columnCount, '+', end='')

# 求出每行的空格数，并放入list中
for j in range(rowCount):
    blankCount = j
    normalList.append(blankCount)
    normalList.sort(reverse=True)
    blankList = normalList

for row in range(1, rowCount+1):
    print(' '*blankList[row-1], end='')
    print('*'*columnList[row-1])


