geshu=int(input('请输入您想的水果个数：'))
shuiguolist=['香蕉']

for i in range(geshu):
    print('第',i+1,'个水果，',end='')            #range是从0开始计数，为显示方便，将0作为第一个数；end 参数是为了和下一行字符输出保持在同一行
    shuiguolist.append(input('请输入名称：'))

else:                                             # for 循环的else 语句，用于超出既定计数后的处理
    print('输入结束！')

del shuiguolist[0]                                # 删除预置的第1个水果项
print('您想要的水果分别是：',shuiguolist)        # 输出刚才已输入的List列表数据
print('另外一种显示方法：')
for item in shuiguolist:
    print(item,end='  ')
