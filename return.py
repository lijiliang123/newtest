def return2():
    n1=int(input('请输入第一个数字：'))
    n2=int(input('请输入第二个数字：'))
    if n1>n2:
        print(n1,'大于',n2)
        return n1
    elif n1==n2:
        print(n1,'等于',n2)
        return n1
    else:
        print(n1,'小于',n2)
        return n2

return2()

# list comprehension, list 的扩展用法
listone=[2,3,4]
listtwo=[]
listtwo=[2*i for i in listone if i>1]
print(listtwo)
print(__name__)
#for i in listone:
#    if i>2:
#        listtwo.append(i*2)

#print(listtwo)

print(pow(2,4))

