import random


def count_sort(nums, max_num):
    """
    当我知道一组数字的范围时.统计该范围内每个数字出现的次数.时间复杂度为 O(n). 这里
    虽然有两个for循环嵌套，但是里面的循环的范围不是 n.
    """
    count = [0] * max_num
    for i in nums:
        count[i] += 1
    nums.clear()
    for idx, val in enumerate(count):
        for i in range(val):
            nums.append(idx)


li = [random.randint(0, 10000) for i in range(100)]
print('排序前：', li)
# 注意 li 是一个对象，函数内对改列表的修改会修改原值
count_sort(li, 10000)
print('排序后：', li)



