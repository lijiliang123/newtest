"""
   10大经典算法
"""


# 1. 冒泡排序算法


def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(1, n - i):
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
    return lst


# example:


num = [2, 9, 8, 4, 3, 7, 6, 10, 20, 18, 19, 1, 0]
print(bubble_sort(num))



