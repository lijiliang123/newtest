import pickle
from collections import deque

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone = record  # 星号(*) 在元组中的应用，星号标出的变量，在输出时是List
print(name)
print(email)
print(phone)

scores = (60, 50, 40, 80, 70)
first, *middle, last = scores  # 星号(*) 在元组中的应用，星号标出的变量，在输出时是List
print(first)
print(last)
print(middle)
print(round(sum(middle) / len(middle)))

# 以下为：序列化文件存储与反序列化文件输出


inputscore = []
count = 0
flag = True
while flag:
    inputscore.append(int(input('请输入多少数字：')))
    count += 1
    if count == 3:
        flag = False
        print('您已输入满', count, '个数字，现在依次输出所输入内容：')
        break

for item in inputscore:
    print(item, '---', end='')

print('')
with open('score.txt', 'wb') as f:
    pickle.dump(inputscore, f)
    print('score.txt文件写入成功！')

with open('score.txt', 'rb') as f:
    content = pickle.load(f)
    print('开始读取score.txt文件')
    if len(content) > 0:
        for i in range(len(content)):
            print(content[i], '---', end='')

print()

abc = deque()
sr = True
count2 = 0
while sr:
    abc.append(int(input('Pls input number:')))
    count2 += 1
    if count2 == 5:
        sr = False

print(abc)
for item2 in abc:
    print(item2, '+++', end='')

print()

d1, *d2, d3 = abc  # 星号在deque()实例中的应用，星号标的变量输出为List列表
print('{0}++{1}++{2}'.format(d1, d2, d3))  # 字符串的格式化输出
