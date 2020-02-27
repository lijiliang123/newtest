# This is my first program in Python.
print("Hello,World!")
print("Hello,Thomas!")
print('{0} is my son, his age is {1}'.format('春晖',8))
print('{0:.6f}'.format(2/3))

print('this is first line,\nthis is second line.')
print("what's your name?")  #字符串输出，用双引号
print('what\'s your name?')  #字符串输出，用单引号＋转义字符\

i=5
print(i)
i=i+1
print(i)
s='''       
this is third line.
this is fourth line
'''           #三个引号，表达多行字符串
print(s)
t = 'hello, hello ,hello,\
 we remeber you forever!'
print(t)


length = 10
width = 8
area = length*width

print('The area is', area)



print('{0:*^120}'.format('The Log File Output End'))



'''
Python数据类型：
1）常量，数值型常量或字符型常量，字符型要用引号括起来
2）int, float
3) string
   字符串可以用单引号，也可以用双引号，多行字符串用三引号
4）format，字符串格式化输出
5) 运算符：＋－* /, **, //, %


'''
