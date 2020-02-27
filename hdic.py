from collections import defaultdict
# 数据字典类型，当一个key对应多个值时，可以使用 defaultdict类，此时可以构建字典的元素为list[], 或者set([]), 或者tuple()
my=defaultdict(list)
you=defaultdict(tuple)
my['a'].append(1)  # 字典对象［KEY］.append（VALUE）
my['a'].append(2)
my['a'].append(3)
my['b'].append(3)
my['b'].append(4)
my['c'].append(3)
my['c'].append(4)



print(my)


#输出字典值列表
for key in my:
    print(key,my[key])

# 使用 OrderedDict类
from collections import OrderedDict

mm=OrderedDict()
mm['foo']=1
mm['coo']=2
mm['boo']=3
mm['doo']=4

for i in mm:
    print(i,mm[i],'*'*10,end='')

