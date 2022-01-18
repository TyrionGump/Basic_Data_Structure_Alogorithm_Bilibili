import random


def shift(nums, low, high):
    '''
    1. 堆必须是一个完全二叉树. 小根堆指任意节点都比其子节点小. 大根堆指任意节点都比其子节点大
    2. 父节点和左子节点的编号关系是 i -> 2i + 1
    3. 父节点和右子节点的编号关系是 i -> 2i + 2
    4. 根据 python 整除向下取整的机制. 左右子节点和父节点的关系是 (i - 1) / 2
    5.
    这里我们不新创建一个列表存储结果，而是继续利用原列表. 因此，需要保存堆的最后一个元素的位置来记录哪些
    元素还没有被排序.

    :param nums: 列表
    :param low: 堆的根结点位置
    :param high: 堆的最后一个元素的位置
    :return:
    '''

    # 利用 i 和 j 记录当前所看节点和其子节点的位置
    i = low
    j = 2 * i + 1  # j 指向左子节点
    tmp = nums[i]  # 把堆顶存下来
    while j <= high:
        if j + 1 <= high and nums[j + 1] > nums[j]:  # 两个子孩子先比大小
            j = j + 1  # j 指向右子节点
        if nums[j] > tmp:  # 子节点中更大的那个和根结点比较
            nums[i] = nums[j]
            i = j
            j = 2 * i + 1
        else:
            nums[i] = tmp  # 把tmp放在中间的某一个节点上
            break
    else:
        nums[i] = tmp  # 把tmp放在叶节点了


def heap_sort(nums):
    n = len(nums)

    # 建立堆
    for i in range((n-2)//2, -1, -1):  # n-1 是最后一定叶节点的索引, (n-2) // 2 是最后一个堆的堆顶索引
        shift(nums, i, n-1)

    # 每次把堆顶（该堆最大的数）和堆的最后一个数字交换. 然后再次调整.
    for i in range(n-1, -1, -1):
        nums[0], nums[i] = nums[i], nums[0]
        new_high = i - 1
        shift(nums, 0, new_high)


li = [random.randint(0, 10000) for i in range(100)]
print('排序前：', li)
# 注意 li 是一个对象，函数内对改列表的修改会修改原值
heap_sort(li)
print('排序后：', li)








