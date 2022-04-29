"""
   A notebook program by Thomas Lee on 2022/4/29
   f.write(str)的参数是一个字符串，就是你要写入文件的内容。
   f.writelines(sequence)的参数是可以是字符串，也可以是字符串序列，比如列表，它会迭代帮你写入文件。
   write(str):把字符串写入文件，单行写入。
   writeline(str):把字符串按行写入文件，多行写入。

"""

start = True
stop = ['q', 'Q', 'quit', 'QUIT', 'n', 'N']
jxin = ['y', 'Y', 'yes', 'YES']
zhwen = []

print('这是一个记事本，请输入你想要保存的内容, 按q, Q, quit, QUIT, n, N键结束输入！')
while start:
    nr = input('#')
    if nr in stop:
        print('你已停止记事本输入！')
        start = False
    else:
        zhwen.append(nr + '\n')  # 加换行符后，写入时自动换行；否则写入时不换行
        continue

title = input('请输入文件名称：')
with open(title + '.txt', 'a', encoding='utf-8') as f:  # 增加文件后缀名.txt
    f.writelines(zhwen)  # writelines的参数可以是个list

"""
    for item in zhwen:
        f.write(item)
        
"""

print('现在输出你已保存的文件：', '<<', title, '>>')
with open(title + '.txt', 'r', encoding='utf-8') as f:
    ot = f.read()
    if len(ot) > 0:
        print(ot)
