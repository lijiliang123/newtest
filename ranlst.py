import random

lt1 = []
numTotal = 10
ctNum = 1

while ctNum <= numTotal:
    lt1.append(random.randint(0, 100))
    ctNum += 1

print('列表总计写入随机数', ctNum-1, '个：')

# 输出列表已写入的随机数
for i in lt1:
    print(i, end=', ')

print('\n将列表正排序后再输出：')
# 将列表元素正排序
lt1.sort()

# 输出列表已写入的随机数
for i in lt1:
    print(i, end=', ')

print('\npop出列表中的最后一个元素：')

lt1.pop()

for i in lt1:
    print(i, end=', ')
