from tkinter import *
import hashlib

root = Tk()
root.title('Thomas Window')
root.geometry('680x680')
lbc = Label(root, text='欢迎您来到新世界!', fg='red', font=('微软雅黑', 20))
lbc.grid(column=1)
lb1 = Label(root, text='用户名：')
lb1.grid(column=0, row=3)
lb2 = Label(root, text='密  码:')
lb2.grid(column=0, row=4)
ipt1 = Entry(root)
ipt1.grid(column=1, row=3)
ipt2 = Entry(root, show='*')
ipt2.grid(column=1, row=4)
lb3 = Label(root)
lb3.grid(column=1, row=10)
strInput = ipt1.get() + ipt2.get()


def hash_fun():
    msg = hashlib.sha256()
    msg.update(str(strInput).encode('utf-8'))
    s = msg.hexdigest()
    lb3.config(text=s, font=('微软雅黑', 20))


cmd = Button(root, text='提交', command=hash_fun)
cmd.grid(column=1, row=6)
root.mainloop()
