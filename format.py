import sys
import os

print('the command line arguments are:')
for i in sys.argv:
    print(i)
print('\nthe python path is:',sys.path,'\n')    #打印系统目录

print(os.getcwd())  # 获取当前工作目录








print('{0} is my son, his age is {1}'.format('春晖',8))
