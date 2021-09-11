import random


def merge(nums, low, mid, high):
    '''
    时间复杂度是 O(nlogn). 有 logn 层， 每层有 n 次操作
    空间复杂度是 O(n). 因为中间有个 ltmp 存结果.
    '''
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if nums[i] < nums[j]:
            ltmp.append(nums[i])
            i += 1
        else:
            ltmp.append(nums[j])
            j += 1

    # 如果左边或者右边没有数字了，将另外一部分依次添加到结果
    while i <= mid:
        ltmp.append(nums[i])
        i += 1

    while j <= high:
        ltmp.append(nums[j])
        j += 1

    nums[low:high+1] = ltmp


def merge_sort(nums, low, high):
    if low < high:  # 至少有两个元素，递归
        mid = (low + high) // 2
        merge_sort(nums, low, mid)
        merge_sort(nums, mid + 1, high)
        merge(nums, low, mid, high)


li = [random.randint(0, 10000) for i in range(100)]
print('排序前：', li)
# 注意 li 是一个对象，函数内对改列表的修改会修改原值
merge_sort(li, 0, len(li) - 1)
print('排序后：', li)