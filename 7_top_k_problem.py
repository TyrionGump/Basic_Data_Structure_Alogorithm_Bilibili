import random
import time
import math

'''
解决思路：
1. 取列表前 k 个元素建立一个小根堆. 堆顶是目前第k大的数
2. 依次向后遍历列表，对于列表中的元素，如果小雨堆顶，则忽略该元素；否则将堆顶更换为该元素，并对堆进行一次调整.
'''

def shift(nums, low, high):
    # 利用 i 和 j 记录当前所看节点和其子节点的位置
    i = low
    j = 2 * i + 1  # j 指向左子节点
    tmp = nums[i]  # 把堆顶存下来
    while j <= high:
        if j + 1 <= high and nums[j + 1] < nums[j]:
            j = j + 1  # j 指向右子节点
        if nums[j] < tmp:
            nums[i] = nums[j]
            i = j
            j = 2 * i + 1
        else:
            nums[i] = tmp  # 把tmp放在中间的某一个节点上
            break
    else:
        nums[i] = tmp  # 把tmp放在叶节点了


def top_k(nums, k):
    heap = nums[0: k]
    # 建立前 k 个元素的堆
    for i in range((k-2)//2, -1, -1):
        shift(heap, i, k - 1)

    # 遍历后续元素看是否需要建堆
    for i in range(k, len(nums)):
        if nums[i] > heap[0]:
            heap[0] = nums[i]
            shift(heap, 0, k - 1)
    # 取出 top k
    for i in range(k-1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        new_high = i - 1
        shift(heap, 0, new_high)

    return heap

start_time = time.time()
li = list(range(10000))
random.seed(1)
random.shuffle(li)
# print('排序前：', li)
# 注意 li 是一个对象，函数内对改列表的修改会修改原值
k = 10
res = top_k(li, k)
print('top-{}: '.format(k), res)
end_time = time.time()
print(end_time - start_time)

print(math.log())