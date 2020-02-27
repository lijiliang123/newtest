'''
: string的实际使用技巧
：python cookbook3
: 2018-10-12

'''
import re
line='asdf fjdk; afed,fjek,asdf, foo'
#使用多个界定符分割字符串
my=re.split(r'[;,\s]\s*', line)
print(my)

m1=tuple(my)  #list type convert into tuple type
print(m1)
m2=list(m1)  #tuple type convert into list type
print(m2)

#文件名匹配检查，返回 True or False
from fnmatch import fnmatch,fnmatchcase
s1='foo.txt'
print(fnmatch(s1,'*.txt'))
print(fnmatchcase(s1,'*.TXT'))

dc=re.compile(r'\d+/\d+/\d+')  # 正则表达式编译后，可以多次调用
# Simple matching: \d+ means match one or more digits
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(dc.match(text))   # match从字符串开始位置进行匹配，此例返回false
print(dc.findall(text)) # findall从字符串任意位置进行匹配，此例返回两个日期['11/27/2012', '3/13/2013']

from calendar import month_abbr
re.IGNORECASE

#sub(被查的特定字符串，替换为字符串，被查找完整字符串，查找时忽略大小写标识)
text2 = 'UPPER PYTHON, lower python, Mixed Python'
print(re.sub('python', 'snake', text2, flags=re.IGNORECASE)) #查找并替换，忽略查找字符串的大小写

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

text3='this is a book.'
print(text3.capitalize(), text3.upper(), text3.lower())

#unicodedata 标准化
import unicodedata
s = '\ufb01' # A single character
print(unicodedata.normalize('NFC',s))
print(unicodedata.normalize('NFD',s))

mm=re.compile(r'\d+')
ss='this is my score 112 113 114'
print(mm.findall(ss))

#strip, lstrip, rstrip，去除空格
gstr='   hello world '
print(gstr.strip())
print(gstr.lstrip())
print(gstr.rstrip())

x = 1.2345
print(format(x, '*>30')) #右对齐，宽度30个字符，空白位置用 * 填充
print(format(x, '*<30')) #左对齐，宽度30个字符，空白位置用 * 填充
print(format(x,'^30.2f')) #居中对齐，2位小数，浮点型

sa='Hello'
sb='everyone'
sc='good afternoon!'
print(sa,sb,sc,sep=': ')
print('{} {}'.format(1,2))

#使用textwrap 模块来格式化字符串的输出
import textwrap
import os
s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."
print(textwrap.fill(s,70,initial_indent='   ')) #格式化成每行70个字符，首行缩进空格

#字节字符串，返回整数不是字符
s = b'Hello World'
print(s)
print(s[0])
print(s.decode('ascii')) #解码后正常输出



