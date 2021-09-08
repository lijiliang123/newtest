while True:
    s=input('请输入任意字符：')
    if s == 'quit':
        print('不好意思，您踩雷了！')
        print('程序结束！')
        break
    elif len(s) < 5:
        print('您输入的字符数太少！')
        continue
    else:
        print('您输入的字符数是：', len(s), '个,', end='')
        print('合乎标准，程序结束！')
        break
