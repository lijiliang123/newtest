# set 是集合(['',''])，list 是列表['','']， tuple 是元组('','')， dict 是字典{'':'','':''}，string 是字符串('')
# set 集合里的元素是没有索引的，是无序的，这区别于上述其它几类：list ， tuple ， dict ，string
# list的方法，包括：append(增加元素）, extend(增加的元素为列表时，实际增加列表中的元素), del(删除索引位的元素)
# list的方法，包括：remove(删除元素本身，不按索引), clear(清空列表的所有元素), pop(元素出栈)
# list的方法，包括：sort(列表元素排序，有key参数=len、reverse参数)

blist = list('thomas lee')
blist.pop()  #pop方法实现列表元素的出栈操作，出栈方式是后进先出
blist.sort(reverse=True)  #sort方法实现列表元素排序，reverse参数指定正向、反向排序
print(blist)

#集合示例
country = set([])  # 空的集合对象赋值
geshu = int(input('请输入您想输入的个数：'))

for i in range(geshu):
    print('现在，请输入第', i+1, '项', end=' ')        # range 计数，是从0开始的，为了显示方便（从第1个数开始，故＋1）
    country.add(input('国家:'))                      # 集合增加新的值，但从输出结果看是无序增加，即没有索引
    if len(country) == 0:
        print('不妙！')
        break
else:
    print('您已完成', geshu, '个国家输入,程序结束！')

#country.remove('')                                  # 删除集合的初始值
print('现在，将您输入的结果进行输出：')          # 因为集合内元素是无序的，所以不能用索引输出
print(country)
