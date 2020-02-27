print('+'*50)  #输出字符多少次

import heapq

num=[21,-2,30,12,50,28,33]

a,*b,c=num
print(a,b,c)

for i in range(len(num)):
    print (num[i],'+'*10,end='')

class PriorQue:
    def __init__(self):
        self._queue=[]
        self._index=0
        print()
        print('开始初始化...')

    def push(self, item, priorty):
        heapq.heappush(self._queue,(-priorty,self._index,item))
        self._index+=1
        print('push 方法')

    def pop(self):
        print('pop 方法')
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)


q=PriorQue()
q.push(Item('foo'),5)
q.push(Item('doo'),4)
q.push(Item('coo'),1)
q.pop()
q.pop()
q.pop()

print('#'*100)



