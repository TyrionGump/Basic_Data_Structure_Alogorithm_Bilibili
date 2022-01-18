import random


def select_sort_simple(nums):
    '''
    这个方法不好的原因:
        1. 需要两倍内存
        2. 循环内部 min 是 O(n)
        3. 循环内部 remove 也是 O(n), 因为找到删除的东西， 而且删除过程要把后面的 push 到前面
    '''
    res = []
    for i in range(len(nums)):
        min_val = min(nums)
        res.append(min_val)
        nums.remove(min_val) # 有重复的也是先删除第一个
    return res

li = [random.randint(0, 10000) for i in range(100)]
print('排序前：', li)
# 注意 li 是一个对象，函数内对改列表的修改会修改原值
sorted_li = select_sort_simple(li)
print('排序后：', sorted_li)


def select_sort(nums):
    '''
    找到最小的之后和最开始的交换
    '''
    res = []
    for i in range(len(nums) - 1):
        min_loc = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_loc]:
                min_loc = j
        if i != min_loc:
            nums[i], nums[min_loc] = nums[min_loc], nums[i]
    return res

li = [random.randint(0, 10000) for i in range(100)]
print('排序前：', li)
# 注意 li 是一个对象，函数内对改列表的修改会修改原值
sorted_li = select_sort(li)
print('排序后：', sorted_li)
