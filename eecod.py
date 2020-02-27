'''
 该示例程序是关于文件编码方式的演示
'''

zifu=input('输入您的内容：')

print('您输入的内容是：',zifu,',[encode转码为：',zifu.encode(),']')
print('您输入的内容是：',zifu,',[utf-8转码为：',zifu.encode('utf-8'),']')
print('您输入的内容是：',zifu,',[gbk转码为：',zifu.encode('gbk'),']')
print('您输入的内容是：',zifu,',[gb18030转码为：',zifu.encode('gb18030'),']')
print('您输入的内容是：',zifu,',[gb2312转码为：',zifu.encode('gb2312'),']')

jiema=b'\xd2\xbb\xd6\xbb\xd0\xa1\xb9\xb7'
print(jiema,'解码为：',jiema.decode('gbk'))

# 倒入第三方包文件
from chardet import detect

with open(r'部署手册.txt',encoding='gb2312') as f:
    names=f.read()
    print(names)

with open(r'部署手册.txt',encoding='gb2312') as f:
    neirong=f.read()
    print(detect(neirong.encode('gb2312')))   #判断打开文件内容是何种编码方式
    print(detect(neirong.encode('utf-8')))    #判断打开文件内容是何种编码方式





