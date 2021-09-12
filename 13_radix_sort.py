import random
import math


def radix_sort(nums):
    """
    时间复杂度 O(kn). k 是要考虑几位数. k = log(10, 最大数的位数)
    因此它有时比前几个 O(nlogn) 快. 因为他们的 logn = log(2, 数字个数).
    空间复杂度 O(n + k).
    """
    max_num = max(nums)
    iter = 0
    while 10 ** iter <= max_num:
        buckets = [[] for _ in range(10)]  # 这里不要用 [[]] * 10, 似乎内部的这些空list append 会对所有list都append
        for val in nums:
            # 提取第几位数
            digit = (val // (10 ** iter)) % 10
            buckets[digit].append(val)
        # 把数字按该次排序后的结果合并
        nums.clear()
        for b in buckets:
            nums.extend(b)

        iter += 1

li = [random.randint(0, 10000) for i in range(100)]
print('排序前：', li)
# 注意 li 是一个对象，函数内对改列表的修改会修改原值
radix_sort(li)
print('排序后：', li)