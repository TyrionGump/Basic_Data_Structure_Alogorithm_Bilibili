import random


def insert_sort(nums):
    for i in range(1, len(nums)): # i 表示摸到的无序区的第几个元素
        j = i - 1
        tmp = nums[i]
        while j >= 0 and nums[j] > tmp:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = tmp


li = [random.randint(0, 10000) for i in range(100)]
print('排序前：', li)
# 注意 li 是一个对象，函数内对改列表的修改会修改原值
insert_sort(li)
print('排序后：', li)