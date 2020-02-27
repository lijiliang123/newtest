def myaverage(*score):
    first,*middle,last=score
    avg=sum(middle)/len(middle)
    print('平均值是：',avg)
    return avg

#myaverage(30,40,50,60,70,80,90,100)
shuzi=''
geshu=int(input('请输入你想要的数字个数：'))
for i in range(geshu):
    print('请输入第',i+1,end='')
    if i+1==geshu:
        shuzi=shuzi+input('个数字：')+'.'
    else:
        shuzi=shuzi+input('个数字：')+','

   # shuzi.append(int(input('个数字：')))

print('你输入的数字是：',shuzi)
#myaverage(x for x in shuzi)
myaverage(shuzi)

#print(myaverage(30,40,50,60,70,80,90,10)

from flask import Flask

Flask.request_context()
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'
