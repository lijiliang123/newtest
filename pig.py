# 跨模块调用函数，先import .py文件（或称为Module）;
# 然后通过点操作符调用.py文件中的函数和成员变量

import sys
import os
import dddretr


print(sys.path)
dddretr.game()
print('The module name is',dddretr._name_)
print('The module version is',dddretr._version_)
print('The module author is',dddretr._author_)
print('The module address is',dddretr._adrress_)

#print('dir is ',sys.path)



