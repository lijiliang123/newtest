# tuple 元组，值不可变，也没有list 拥有的强大方法（apend, del, remove等）
# dictionary 字典，值不可变，也没有list 拥有的强大方法（apend,  remove等）

# 以下是dtuple 元组的例子：
zoo=('河马','狮子','老虎','大象')
print('动物园的动物有：',len(zoo),'种,',end=' ')
print('它们分别是：',zoo)
print('其中第2种动物是：',zoo[1])

myzoo=('',)
geshu=int(input('请输入您想要的动物数量：'))
for i in range(geshu):
    myzoo=(str(input('请输入你喜欢的动物名称:')))


print('您输入的动物总数是：',len(myzoo)+1)
for d in range(len(myzoo)):
    print(myzoo)


#print('您输入的动物名称是：',myzoo.)


