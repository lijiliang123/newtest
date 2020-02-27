#实现一个电话本，屏幕录入联系人信息，并写入文件，可查看、修改、删除操作。

import os
import time
import pickle

#文件名和存储路径
filename='电话本.txt'
filedir='d:\\PycharmProjects\\test'
filepath=filedir+os.sep+filename
print('电话本存储路径是：',filepath)
content={':':'-'}

class contactbook:


    def __init__(self,name,sex,age,address,phone):
        self.name=name
        self.sex=sex
        self.age=age
        self.address=address
        self.phone=phone
        print('联系薄对象初始化中......')

    def inputcontactbook(self):
        isinput=True
        while isinput:
            self.name=str(input('请输入联系人姓名：'))
            self.sex=str(input('请输入联系人性别：'))
            self.age=str(input('请输入联系人年龄：'))
            self.address=str(input('请输入联系人地址：'))
            self.phone=str(input('请输入联系人电话：'))

            #content=content+str(self.name)+str(self.sex)+str(self.age)+str(self.address)+str(self.phone)

            # dict 的赋值 key=value
            content[str(self.name)]='姓别：'+str(self.sex)+' '+\
                                         '年龄：'+str(self.age)+' '+\
                                         '地址：'+str(self.address)+' '+\
                                         '电话：'+str(self.phone)+' '

            f=open(filename,'wb')
            #f.write(content)
            pickle.dump(content,f)
            f.close()
            f=open(filename,'rb')
            storedcontent=pickle.load(f)

            #del content['']  #删预置的第1条数据，按key删除
            print(storedcontent)

            s=input('您还要继续输入吗？请回答Y/N：')
            if s=='N':
                print('您已退出登记薄输入程序！')
                isinput=False
                f.close()
                break
            elif s=='n':
                break
            else:
                continue

# 类实例化：
mycontactbook=contactbook('','','','','')

# 类方法调用：
mycontactbook.inputcontactbook()









