# import random
#
#
# def partition(nums, left, right):
#     tmp = nums[left]
#     while left < right:
#         # 从右往左滑动游标, 这里 left < right 是有可能 right 出了列表导致 nums[right]报错
#         while left < right and nums[right] >= tmp:
#             right -= 1
#         nums[left] = nums[right]
#         while left < right and nums[left] <= tmp:
#             left += 1
#         nums[right] = nums[left]
#     nums[left] = tmp
#     return left  # 此时 left = right 返回哪个都行
#
#
# def quick_sort(nums, left, right):
#     '''
#     将原列表疯狂二分. 复杂度为 O(nlogn). 但是在最坏情况下 (反向排序好的列表), 此时每次切分其实都切成
#     一个原列表减一个元素和另一个是一个元素. 此时时间复杂度会 n^2. 为了避免这个情况可以在 partition 函数中不选择第一个作为 tmp,
#     而是随机抽取一个.
#
#     这个算法还有个问题. 递归会占用大量资源.
#     '''
#     if left < right:  # 只考虑列表里有大于或等于两个元素的情况 (不然只有一个元素的时候根本不用考虑排序)
#         mid = partition(nums, left, right)
#         quick_sort(nums, left, mid - 1)
#         quick_sort(nums, mid + 1, right)
#
#
# li = [random.randint(0, 10000) for i in range(100)]
# print('排序前：', li)
# # 注意 li 是一个对象，函数内对改列表的修改会修改原值
# quick_sort(li, 0, len(li) - 1)
# print('排序后：', li)

import pandas as pd
import numpy as np

df = pd.DataFrame()
filtered_feature = []
for col in df.columns:
    feature_stats = df[col].value_counts(dropna=True, normalize=True)
    if 'NaN' in feature_stats.index and feature_stats.loc[:, 'Nan'] > 0.5:
        continue
    else:
        filtered_feature.append(col)
df = df[filtered_feature]


