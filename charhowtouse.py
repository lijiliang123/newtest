"""
    This python file is shown how to use the Character function.
    It includes all kinds of character usage.
    It is from a web article.
    Let's begin from March, 31st, 2022.
"""
'''
    ///第一部分：字符串切片操作///
'''

test = "python programming"
print("The string is: ", test)
for i in range(len(test)):
    print(test[i], '--', end='')
print()

# 输出首字母
first_char = test[:1]
print("The first character of the string is:", first_char)
# 输出尾字母
last_char = test[-1:]
print("The last character of the string is:", last_char)

# 输出除去首字母的所有字符
except_char = test[1:]
print("The except first character of the string is:", except_char)
# 输出除去尾字母的所有字符
except_last = test[:-1]
print("The except last character of the string is:", except_last)
# 输出首字母和尾字母中间的所有字符
between_two = test[2:-2]
print("The between two character of the string is:", between_two)

#跳过一个字符输出
skip_one = test[0:18:2]  #[start:stop:step]
print("The skip one character of the string is:", skip_one)
#反转输出字符串
reverse_char = test[::-1]
print("The reverse character of the string is:", reverse_char)


'''
    ///第二部分：检查字符串是否为空///
'''

import re
from collections import Counter

sentence = "Canada is located in the northern part of North America"
counter = len(re.findall('a', sentence))
print(counter)
counter = sentence.count('a')
print(counter)
