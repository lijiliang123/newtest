"""
    本程序示例字符串常用操作方法

"""

n = 3.1415926535
s1 = 'thomMS lee'
s2 = '   this is a dog.com  '
print('the number value is {}'.format(n))
# 格式：字符串（含%）+%+变量
#字符串中的%后面必须有数据类型：s-字符串，f-浮点数值, d-整型
print('the number %s value is %-6.2f' % (s1, n))  #宽度为6个字符，-代表左对齐，.2代表精度2位小数，f代表输出浮点数
print('the number value is %-6.3f' % n)
print('the number value is %-6.3s' % s1)  #.3s代表输出类型为字符串变量中的3个字符
print('abc' in s1)   #判断s1字符串中，是否包含'abc'子串，使用in关键字
print(s1.upper())  #字符串转为所有字母大写
print(s1.title())  #字符串转为首字母大写
print(s1.lower())  #字符串转为所有字母小写
print(s2.strip())  #删除字符串左右两边的空格
print(s2.lstrip())  #删除字符串左边的空格
print(s2.rstrip())  #删除字符串右边的空格
print(s2.startswith('this'))  #判断字符串是否以this开头，返回False
print(s2.endswith('dog'))  #判断字符串是否以dog结尾，返回False
print(s2.find('this'))  #返回this子串在字符串中出现的位置3
print(s2.replace('dog', 'cat'))  #将字符串中的dog，替换为cat
print(s2.split())  #用空格作为分隔符对字符串操作，返回list
print(s2.split('.'))  #用.作为分隔符对字符串操作，返回list
mylist = s2.split()
print('/'.join(mylist))  #分隔后的字符串用/连接起来
print(','.join(mylist))  #分隔后的字符串用,连接起来
