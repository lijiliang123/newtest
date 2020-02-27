'''
 一个例子：集合 deque, 内容以序列化写入文件，并反序列化读出
'''
from collections import deque
import pickle
#deque类型初始化
acollection=deque()

jixu=True

# begining to input item:
while jixu:
    item=input('请输入任何字符：')
    if item=='0':
        print('输入0代表停止输入！',end='')
        if len(acollection)==0:
            print('您什么都没有输入！')
        jixu=False
    else:
        acollection.append(item)
else:
    print('您的输入已结束！')

# begining output item
if len(acollection)==0:
    print('')
else:
    print('现在开始输出您输入的字符：')
    for i in range(len(acollection)):
        print(acollection[i],'-',end=' ')

print('\n')

if len(acollection)==0:
    print('')
else:
    with open('文件deque.txt','wb') as f:
        pickle.dump(acollection,f)
        print('文件deque.txt写入成功！')

if len(acollection)==0:
    print('')
else:
    print('现在输出文件内容：')

    with open('文件deque.txt','rb') as f:
        content=pickle.load(f)
        for i in range(len(content)):
            print(content[i],'++',end=' ')

#    print(content)
#    while True:
#        s=f.readline()
#        if len(s)==0:
#            break
#        else:
#            print(s)
        print('\n文件输出结束！')


