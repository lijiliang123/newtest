#元组与参数字典  的函数定义

def mytest(a=5,*numbers,**phonebook):
    print('a=',a)
    for single_number in numbers:
        print('single number is ',single_number)
    for first_part,second_part in phonebook.items():
        print(first_part,':',second_part)

mytest(4,2,3,5,9,6,thomas=123,john=456,mike=345)
