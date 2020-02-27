#网络传输过程中，只能以二进制形式传送数据，将对象变成二进制存储叫序列化，将二进制文件转换成对象叫反序列化
import pickle

fdata = 'shoplist.data'
shoplist = ['banana','apple','pearl']

f = open(fdata, 'wb')

#将对象shoplist序列化：
pickle.dump(shoplist, f)
f.close()

del shoplist
f = open(fdata,'rb')

#将文件中存储的对象shoplist反序列化：
storedlist = pickle.load(f)

print(storedlist)
try:
    s=input('Pls input someting:')
except:
    print('ERROR,ERROR!')
else:
    print('You have inputed:{}'.format(s))
