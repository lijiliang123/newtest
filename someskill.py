very = 10, 20, 30, 40, 50
print(very)  #序列封包成元组（, , ）

fir, sec, *rest = very  #序列解包并赋值
print(type(fir), fir)
print(type(sec), sec)
print(type(rest), rest)
tlist = list(very)  #元组对象转换为列表对象
print(tlist)

#元组、列表的相互转化

atuple = range(1, 10)
print(atuple)
alist = list(range(1, 10))
print(alist)
