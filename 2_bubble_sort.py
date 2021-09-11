import random


def bubble_sort(nums):
    # 开始排第几大或者小的元素
    for i in range(len(nums) - 1):
        # 开始从无序元素集中搜索
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                # python 可以直接交换，不用设置第三个变量. python 这个方法实现的底层也不是定义三个变量
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


li = [random.randint(0, 10000) for i in range(100)]
print('排序前：', li)
# 注意 li 是一个对象，函数内对改列表的修改会修改原值
bubble_sort(li)
print('排序后：', li)


def improve_bubble_sort(nums):
    '''
    如果在扫描一遍列表后发现已经排好序了，我们就停止后续排序.
    '''
    # 开始排第几大或者小的元素
    for i in range(len(nums) - 1):
        change_flag = False
        # 开始从无序元素集中搜索
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                # python 可以直接交换，不用设置第三个变量. python 这个方法实现的底层也不是定义三个变量
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                change_flag = True
        if not change_flag:
            return
