class Node:
    """
    链表是由一系列节点组成的元素集合. 每个节点包含两部分, 数据域和指向下一个节点的指针.
    通过节点之间的相互连接, 最终串联成一个链表.
    """
    def __init__(self, item) -> None:
        self.item = item
        self.next = None

def create_linklist_head(nums):
    """
    前插法. 新节点插到头部. head指针指向新节点
    """
    head = Node(nums[0])
    for element in nums[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

def create_linklist_tail(nums):
    """
    尾插法. 新节点插到尾部. tail指针指向新节点
    """
    head = Node(nums[0])
    tail = head
    for element in nums[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

def print_linklist(lk):
    print("===========")
    while lk:
        print(lk.item)
        lk = lk.next

a = create_linklist_head([1, 2, 3])
b = create_linklist_tail([1, 2, 3])

print_linklist(a)
print_linklist(b)