import random


def insert_sort_gap(nums, gap):
    for i in range(gap, len(nums)):
        j = i - gap
        tmp = nums[i]
        while j >= 0 and tmp < nums[j]:
            nums[j + gap] = nums[j]
            j -= gap
        nums[j + gap] = tmp


def shell_sort(nums):
    '''
    对每次一定间隔的元素分别进行插入排序.
    希尔排序的时间复杂度比较复杂，和选取gap的方式有关. 本例子中的方法的最坏情况是 O(n^2).
    一般是在 O(n) 和 O(n^2).
    '''
    d = len(nums) // 2
    while d >= 1:
        insert_sort_gap(nums, d)
        d //= 2


li = [random.randint(0, 10000) for i in range(100)]
print('排序前：', li)
# 注意 li 是一个对象，函数内对改列表的修改会修改原值
shell_sort(li)
print('排序后：', li)