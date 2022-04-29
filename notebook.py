"""
   A notebook program

"""

start = True
stop = ['q', 'Q', 'quit', 'QUIT', 'n', 'N']
jxin = ['y', 'Y', 'yes', 'YES']

while start:
    print('这是一个记事本，请输入你想要保存的内容, 按enter键结束输入！')
    nr = input('开始输入：')
    if nr in stop:
        print('你已退出程序！')
        break

    title = input('请输入文件名称：')
    with open(title, 'a', encoding='utf-8') as f:
        f.write(nr)
    print('现在输出你已保存的文件：', '<<', title, '>>')
    with open(title, 'r', encoding='utf-8') as f:
        ot = f.read()
        if len(ot) > 0:
            print(ot)

    jx = input('要继续写吗？y/n：')
    if jx in jxin:
        continue
    if jx in stop:
        start = False
        print('你已退出程序！')



