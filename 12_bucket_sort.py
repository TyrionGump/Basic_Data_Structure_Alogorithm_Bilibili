import random


def bucket_sort(nums, n=100, max_num=10000):
    """
    时间复杂度取决于数据的分布. 平均情况时间复杂度为 O(n+k). 最坏情况时间复杂度为 O(n^2k). k 大概表示一个桶有多少个数
    空间复杂度为 O(nk)
    """
    buckets = [[]] * n
    for val in nums:
        i = min(val // (max_num // n), n - 1)  # 把数字放在第几个桶，同时考虑超出桶范围的数字放最后一个桶
        buckets[i].append(val)
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    nums.clear()
    for b in buckets:
        nums.extend(b)


li = [random.randint(0, 10000) for i in range(100)]
print('排序前：', li)
# 注意 li 是一个对象，函数内对改列表的修改会修改原值
bucket_sort(li, 100, 10000)
print('排序后：', li)


