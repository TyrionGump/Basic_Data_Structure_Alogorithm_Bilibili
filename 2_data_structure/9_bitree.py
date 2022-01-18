# -*- coding: utf-8 -*-
"""
@File:Basic_Data_Structure_Alogorithm_Bilibili-PyCharm-9_bitree.py
@Date: 29/9/21
@Author: Yubo Sun
@E-mail: tyriongump@gmail.com
@Github: TyrionGump
"""


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return self.data

"""
            E
         /     \
        A       G
           \      \
            C       F
          /   \
        B       D

"""

a = BiTreeNode('A')
b = BiTreeNode('B')
c = BiTreeNode('C')
d = BiTreeNode('D')
e = BiTreeNode('E')
f = BiTreeNode('F')
g = BiTreeNode('G')

root = e
e.left = a
e.right = g
a.right = c
g.right = f
c.left = b
c.right = d

"""
二叉树的遍历方式：
    1. 前序遍历(preorder): EACBDGF
    2. 中序遍历(in order): ABCDEGF
    3. 后序遍历(postorder): BDCAFGE
    4. 层次遍历(level order): EAGCFBD
"""


# def pre_order(tree_node: BiTreeNode):
#     if tree_node:
#         print(tree_node.data, end=',')
#         pre_order(tree_node.left)
#         pre_order(tree_node.right)
#
#
# pre_order(root)


def in_order(tree_node: BiTreeNode):
    if tree_node:
        in_order(tree_node.left)
        print(tree_node.data, end=',')
        in_order(tree_node.right)


in_order(root)


# def post_order(tree_node:BiTreeNode):
#     if tree_node:
#         post_order(tree_node.left)
#         post_order(tree_node.right)
#         print(tree_node.data, end=',')
#
#
# post_order(root)


from collections import deque

def level_order(tree_node:BiTreeNode):
    queue = deque()
    queue.append(tree_node)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=',')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


level_order(root)