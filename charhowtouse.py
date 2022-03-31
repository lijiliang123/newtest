"""
    This python file is shown how to use the Character function.
    It includes all kinds of character usage.
    It is from a web article.
    Let's begin from March, 31st, 2022.
"""

test = "python programming"
print("The string is: ", test)
for i in range(len(test)):
    print(test[i], '--', end='')
print()

first_char = test[:1]
print("The first character of the string is:", first_char)
last_char = test[-1:]
print("The last character of the string is:", last_char)

