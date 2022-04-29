"""
    this is a demo for beginner

"""
import re


textContent = """
It is a beautiful, sunny afternoon. Alice and her sister are sitting by the river. Alice's sister is reading a book. Alice has nothing to do. She looks at her sister's book. There are no pictures in it. 
'And what's the use of a book without pictures?' Alice thinks. 
It is very, very hot. Alice is sleepy. Suddenly she sees a White Rabbit with pink eyes. 
'Oh dear! Oh dear! I'm late!' he says. 
The White Rabbit takes a watch out of his pocket and looks at it. 
'A rabbit with a watch? That's very strange!' thinks Alice.
Alice follows the Rabbit across a field into a big rabbit hole and down, down, down. Alice falls down quite slowly. Around her she can see bookshelves, maps and pictures. She takes a jar from a shelf. 'Orange Marmalade'. She opens it but it is empty. She puts it back.
Down, down, down. 'I'm getting near the centre of the earth,' says Alice, 'I'll meet people that walk with their heads downwards! I'll ask them: "Excuse me, is this New Zealand or Australia?'" 
"""

with open('a.txt', 'w', encoding='utf-8') as f:
    f.write(textContent)

with open('a.txt', 'r') as f:
    nr = f.read()
    if len(nr) > 0:
        print(nr)

    counter = re.findall('A', nr)
    print(len(counter))

print('下面用另一种方式打开文件并输出：')
f = open('a.txt')
data = f.read()
print(data)

f.close()

