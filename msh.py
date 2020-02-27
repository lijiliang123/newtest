"""
    简单copy与深度copy的区别示例

"""
from thomas import jisuan as ji
import copy
origin = [1, 2, [3, 4]]
sel = input('请选择1-浅copy, 2-深度copy: ')
if int(sel) == 1:
    cop = copy.copy(origin)
    print('以下是浅copy的结果，两者指向同一内存块，值相同：')
else:
    cop = copy.deepcopy(origin)
    print('以下是深度copy的结果，两者指向不同内存块，值不同：')

origin[2][0] = "hey!"
#origin[0] = "a"
print('copy前: {}*****copy后: {}'.format(origin, cop))

s1 = int(input('Pls input any number1:'))
s2 = int(input('Pls input any number2:'))

print('You got the sum is: ', ji.he(s1, s2))
print('You got the cha is: ', ji.cha(s1, s2))
print('You got the ji is: ', ji.ji(s1, s2))
print('You got the shang is: ', ji.divd(s1, s2))
