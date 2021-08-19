import numpy as np
import pandas as pd

'''
一维数组：
pd.Series(data=None, index=None, dtype=None)
参数：
data：传入的数据，可以是ndarray、list等
index：索引，必须是唯一的，且与数据的长度相等。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
dtype：数据的类型

二维数组：
DataFrame是一个类似于二维数组或表格(如excel)的对象，既有行索引，又有列索引
pd.DataFrame(data=None, index=None, columns=None)
参数：
index：行标签。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。
columns：列标签。如果没有传入索引参数，则默认会自动创建一个从0-N的整数索引。


'''
# Series 一维数组
aa = pd.Series(np.arange(10))
print(aa)

data = pd.Series([6.7, 5.6, 3, 10, 2], index=[1, 2, 3, 4, 5])
print(data)

color_count = pd.Series({'red': 100, 'blue': 200, 'green': 500, 'yellow': 1000})
print(color_count)
print(color_count.index)
print(color_count.values)

# DataFrame 二维数组
bb = pd.DataFrame(np.random.randn(2, 3))  # 定义2行，3列的二维数组
print(bb)

# 生成10名同学，5门功课的数据
# np.random.randint(最小值,最大值, (行数，列数))
score = np.random.randint(40, 100, (10, 5))  # 均匀分布x
score_df = pd.DataFrame(score)

# 构造行索引序列
subjects = ["语文", "数学", "英语", "政治", "体育"]

# 构造列索引序列
stu = ['同学' + str(i) for i in range(score_df.shape[0])]

# 添加行索引
data = pd.DataFrame(score, columns=subjects, index=stu)
print(data)
print(data.T)           # 将数据转换为table展示
print(data.head(5))     # 展示数据的前5行
print(data.tail(5))     # 展示数据的后5行

df = pd.DataFrame({'month': [1, 4, 7, 10],
                   'year': [2012, 2014, 2013, 2014],
                   'sale':[55, 40, 84, 31]})
print(df)
print(df.set_index('month', drop=True))
print(df.set_index(['year', 'month'], drop=True))

arrays = [[1, 2, 3], ['a', 'b', 'c'], 33, 44]
for a in range(len(arrays)):
    print(arrays[a], end='++')

print('\n')

for a in arrays:
    print(a, end='**')
