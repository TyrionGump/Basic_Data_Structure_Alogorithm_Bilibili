import random
import heapq

nums = list(range(1000))
random.shuffle(nums)
print('原始列表: ', nums)
heapq.heapify(nums)  # 建立堆 (默认是小根堆)
print('建堆后的列表: ', nums)

for i in range(len(nums)):
    print(heapq.heappop(nums), end=',')  # 每次弹出一个最小值, 注意这里是pop因此原列表中的元素会逐渐减少
