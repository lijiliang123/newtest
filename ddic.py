# 下面是一个dictionary 的例子，利用屏幕输入的数据，创建了一个联系人登记本；并将输入的数据输出到屏幕上。
# 字典dict的主要方法，包括：clear(清空字典元素), get(通过key获取value), update(通过key更新value)
# 字典dict的主要方法，包括：items(获取字典所有的key-value对), keys(获取字典所有的key), values(获取字典所有的value)
# 字典的items(), keys(), values() 方法的结果可以转换为list列表, pop（通过key将元素出栈）

nm = 0
ad = 1
di = {}.fromkeys([nm, ad], 'thomas')  #使用fromkeys方法为字典赋初始值
print(di)

dic1 = {'数学': '90', '语文': '95', '英语': '100'}
dic1['历史'] = 100  #字典追加元素
dic1['化学'] = 78  #字典追加元素
dic1['物理'] = 40  #字典追加元素
print(dic1)  #显示成功追加元素
print('语文成绩是：', dic1['语文'])
print('英语成绩是：', dic1.get('英语'))

print('科目 ', ' 成绩')
print('='*11)  #输出11个=符号
for km, cj in dic1.items():
    #print(km, cj)
    print('%s%6s' % (km, cj))  #%6s, 代表输出6个占位符的宽度，变量为字符型，右对齐方式


nmad = {}  #创建空的字典变量，直接用{}
geshu = int(input('请输入您要输入的联系人个数：'))

for i in range(geshu):
    print('请输入第', i+1, '个联系人信息：', end='')
    nmad[str(input('请输入姓名：'))] = str(input('请输入地址：'))     # key=value 赋值形式
else:
    print('您共输入了 ', geshu, ' 条记录,输出您的输入已结束！现在您输入的结果。')
    print('-'*40)  #输出40个-字符

#del nmad['']         #删预置的第1条数据，按key删除

print('姓名  ', '城市   ')

for name, addrss in nmad.items():
    print(name, ' ', addrss)

print(nmad.items())  #获取字典所有的key, value对
keylt = list(nmad.keys())  #获取字典key后，将其转化为list对象
valuelt = list(nmad.values())  #获取字典value后，将其转化为list对象
print(keylt)
print(valuelt)


