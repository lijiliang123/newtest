import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

das = pd.read_csv('Uscore.csv', usecols=['语文', '数学', '英语'])
print(das)
# das.set_index(['语文', '数学', '英语', '体育'])
# print(das['语文']['李四'])
print(das['语文'][1])     # 引用索引，先列后行
print(das.loc['0':'1', '语文'])  # 使用loc:只能指定行列索引的名字，先行范围，再列

das.plot(kind='bar')
plt.show()

das['语文'].plot(kind='bar')
# plt.grid()  #增加网格线
plt.show()

das['数学'].plot(kind='line')
plt.show()
