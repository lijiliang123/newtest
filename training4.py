from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

root = Tk()
root.title("Thomas Windows")
root.geometry('480x480')
lb = Label(root, text='Hello', fg='red', font=('宋体', 32))
ip = Entry(root)
lb2 = Label(root)


def run():
    s = ip.get()
    lb2.config(text=s, font=('宋体', 25))


btn = Button(root, width=10, height=1, relief=RAISED, text='提交', command=run)
lb.place(relx=0.2, y=80, relheight=0.4, width=200)
lb.pack()
lb2.pack()
ip.pack()
btn.pack()

root.mainloop()

