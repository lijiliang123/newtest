import pandas as pd
from matplotlib import pyplot as plt
import math


price = pd.read_csv('price.csv')
idx = price.set_index('年月')   # 横轴上展示年月名称
print(idx)
idx.plot(kind='bar', figsize=(15, 8), fontsize=10, colormap="cool")
plt.show()



