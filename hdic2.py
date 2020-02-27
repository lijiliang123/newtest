str='abc|def|hijk|lmon|'
my=str.split('|')
print(my)

rows = [
{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
{'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
{'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))   #sorted 内置函数实现排序，索引用itemgetter()方法
for item in rows_by_fname:
    for dic in item:
        print(' ',dic,':',item[dic])

    print('*'*15)

    #print(item)

tt=min(rows, key=itemgetter('uid'))     #itemgetter()方法，也适用于min(),max()比较运算
print(tt)
#print(rows_by_fname)

words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]
from collections import Counter
word_counts = Counter(words)
# 出现频率最高的3 个单词
top_three = word_counts.most_common(3)
top_four = word_counts.most_common(4)
print(top_three)
print(top_four)

# 列表元素实现排序, 列表推导
mylist=[1, 4, -5, 10, -7, 2, 3, -1]
pos=[n for n in mylist if n>0]   #简洁表达式，::列表推导::------列表的条件判断＋赋值
print(pos)
for x in pos:
    print(x)
print('-'*10,'排序前的情况：','-'*10)
print(mylist)
print('-'*10,'排序后的情况：','-'*10)
mylist.sort()
print(mylist)
print('-'*10,'列表中大于0的数字：','-'*10)
for i in mylist:
    if i>0:
        print(i,'  ',end='')
print()
print('-'*10,'列表中小于0的数字：','-'*10)
for i in mylist:
    if i<0:
        print(i,'  ',end='')

#filter内置函数
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x=int(val)
        return True
    except ValueError:
        return False
ivals=list(filter(is_int,values))   #过滤结果转换成list类型，类型转换
print()
print(ivals)

#字典推导示例
prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200} #简洁表达式，::字典推导::------字典的条件判断＋赋值
# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
p2 = {key: value for key, value in prices.items() if key in tech_names}

#生成器表达式作为输入参数
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)  #计算平方和
s2=sum(x for x in nums)
print(s,s2)

#求list里的最小值
portfolio = [
{'name':'GOOG', 'shares': 50},
{'name':'YHOO', 'shares': 75},
{'name':'AOL', 'shares': 20},
{'name':'SCOX', 'shares': 65}
]

min_shares=min(portfolio,key=itemgetter('shares'))
print(min_shares)

#两个字典的合并，使用collections.ChainMap()方法
a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }
from collections import ChainMap
c = ChainMap(a,b)
print(c)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)
