import pickle
import os

class hello:
     #实例初始化时调用方法
    def __init__(self,name):
        self.dd=name
        self.sd=name+':'+name

    #无参数方法，Python类的方法的参数列表，必须至少有一个self 参数，调用时则可以不赋值，相当于JAVA中的this
    def hhle(self):
        print('Hi, this is my python class. my name is ',self.dd, '. The sd is',self.sd)
        print(os.path)


#类的实例化
myhello=hello('thomas')
#实例调用类的方法
myhello.hhle()


class human:
    #实例初始化时调用方法
    def __init__(self,name,address,age):
        self.name=name
        self.address=address
        self.age=age
        print('人类初始化:{}'.format(self.name))

    def tell(self):
        '''打印出父类详细情况'''
        print('name:{},address:{},age:{}'.format(self.name,self.address,self.age),end=' ')

#父类human派生类man
class man(human):
    #子类man实例初始化时调用方法
    def __init__(self,name,address,age,huzi):

        #子类调用父类初始化的方法
        human.__init__(self,name,address,age)
        self.huzi=huzi
        print('男人初始化:{}'.format(self.name))

    def tell(self):
        human.tell(self)
        print('huzi:{}'.format(self.huzi))

#父类human派生类woman
class woman(human):
    #子类woman实例初始化时调用方法
    def __init__(self,name,address,age,breast):

        #子类调用父类初始化的方法
        human.__init__(self,name,address,age)
        self.breast=breast
        print('女人初始化：{}'.format(self.name))

    def tell(self):
        human.tell(self)
        print('breast:{}'.format(self.breast))

m1=man('关羽','成都',35,'胡子长')
m2=man('张飞','成都',33,'胡子短')
m3=man('刘备','成都',40,'胡子短')
w1=woman('小乔','苏州',23,'漂亮')
w2=woman('曹鹅','苏州',25,'孝顺')

print()

members=[m1,m2,m3,w1,w2]

for member in members:
    member.tell()

print('输出结束！')


# 下面是另一段 try ...except...finally 异常处理程序, 该代码段也可以被 with 语句代替
try:
    flnm=u'三国人物.txt'
    f=open(flnm,'wb')
    pickle.dump(m1,f)

    #f.write(members)
    f.close()
    f=open(flnm,'rb')
    store=pickle.load(f)
    print(store)

except:
    print('代码出错了!')

finally:
    f.close()
    print('File is closed.')


# 上面的 try ...except...finally 异常处理程序, 也可以被 with 语句代替

with open(flnm,'rb') as f:
    for line in f:
        print(line)


class abc:
    def __init__(self, name, add, age):
        self.name = name
        self.add = add
        self.age = age
        print('The class abc is intializing...')

    def call(self):
        print('class function is calling now!')
        print('My name is ', self.name, ',', end='')
        print('and I live in ', self.add, ',', end='')
        print('and I am', self.age, 'years old.')
        #print('My name is {}:I live in {}:I am {} years old.'.format(self.name, self.add, self.age))


ruotong = abc('Guanruotong', 'Guangzhou', 5)
ruotong.call()
chunhui = abc('Chunhui', 'Guangzhou', 10)
chunhui.call()
