# -*- coding: utf-8 -*-
"""
@File:Basic_Data_Structure_Alogorithm_Bilibili-PyCharm-8_hash_list.py
@Date: 28/9/21
@Author: Yubo Sun
@E-mail: tyriongump@gmail.com
@Github: TyrionGump
"""

"""
直接寻址表： key 为 k 的元素放到 k 位置上 -> 造成一定程度的浪费
hashing: key 为 k 的元素放到 h(k) 位置上

解决哈希冲突的两种方向：
    1. 开放寻址法：往后找空位
    2. 拉链法：在冲突位置开链表
"""


# 一个功能更多的链表
class LinkList:
    class Node:
        def __init__(self, item=None):
            self.item = item
            self.next = None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        return self.LinkListIterator(self.head)

    def __repr__(self):
        return "<<" + ", ".join(map(str, self)) + ">>"


class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.Table = [LinkList() for i in range(self.size)]

    def h(self, k):
        return k % self.size

    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print('Duplicated Insert!')
        else:
            self.Table[i].append(k)

    def find(self, k):
        i = self.h(k)
        return self.Table[i].find(k)

ht = HashTable()
ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(102)
print(",".join(map(str, ht.Table)))


