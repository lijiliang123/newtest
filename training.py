import random

#注意sorted(), reversed()函数，与list的sort(), reversed()方法的区别
#前者对列表不做物理顺序改变，只是展现上做了改变； 但后者对列表做了物理改变
#以下为示例程序
mls = [x for x in range(10)]  #列表推导式的应用
for item in mls:
    print(item, end='\t')
print()
print('使用sorted()函数的结果')
nls = sorted(mls, reverse=True)
print(nls)
print('使用reversed()函数的结果')
rls = reversed(mls)
for x in rls:
    print(x, end='\t')
print()
print('显示原list, 证明：sorted函数和reversed函数对原列表不产生影响')
print(mls)
print('但是list的sort()方法，则会对原列表产生实质影响，将原元素实现永久排序')
mls.sort(reverse=True)
print(mls)

#另一个程序，展现列表、元组的初始化，列表元素的赋值与排序，列表与元组对象类型的互相转化
changdu = int(input('请输入您要的列表或元组长度(1000以内)：'))
ls = []  #列表对象赋空值
tu = ()  #元组对象赋空值
i = 0
while i < changdu:
    num = random.randint(0, 1000)
    #列表元素只能为奇数的判断
    if num % 2 > 0:
        ls.append(num)
    else:
        ls.append(num+1)
    #ls.append(random.randint(0, 1000))
    i += 1

print('1.现在输出列表长度为', changdu, '的列表项，先不排序：')

for n in range(len(ls)):
    print(ls[n], end='  ')

print()  #回车

#对生成的列表项元素先排序，再输出
print('2.现在对列表元素进行排序，并输出排序后的结果：')
ls.sort()  #使用列表的sort方法，实现列表元素的排序
for n in range(len(ls)):
    print(ls[n], end='  ')

print()
tu = tuple(ls)  #将列表对象转换为元组对象
print('3.现在输出将列表转换为元组后，元组的元素：')
for x in range(len(tu)):
    print(tu[x], end='  ')

print()
print('4.另外一种元组、列表的输出方法：')  #与上面第3点的索引访问法不同
for x in tu:
    print(x, end='  ')

print()
print('列表:', ls)
print('元组:', tu)

ls2 = [x * x for x in range(10) if x % 2 == 0]  #列表推导式示例
print(ls2)
print(sum(ls2))  #list中的所有元素求和
print(max(ls2))  #list中元素的最大值
print(min(ls2))  #list中元素的最小值

#匿名函数lambda示例
hf = lambda a, b: a*b  #lambda 函数可以使用任意数量的参数，但表达式只能有一个
print('lambda匿名函数应用：', hf(2, 3))


