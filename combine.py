# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？

def threeNums():
    count = 0
    nums = []
    for index1 in range(1, 5):
        for index2 in range(1, 5):
            for index3 in range(1, 5):
                if index1 != index2 and index1 != index3 and index2 != index3:
                    num = 100 * index1 + 10 * index2 + index3
                    if num not in nums:
                        nums.append(num)
                        count += 1
    print(count)
    print(sorted(nums))


threeNums()


