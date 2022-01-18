# -*- coding: utf-8 -*-
"""
@File:Basic_Data_Structure_Alogorithm_Bilibili-PyCharm-10_binary_serach_tree.py
@Date: 29/9/21
@Author: Yubo Sun
@E-mail: tyriongump@gmail.com
@Github: TyrionGump
"""

"""
二叉搜索树性质：左子节点数字小于父节点数字；右子节点数字大于父子节点数字
"""


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                # self.root = self.insert(self.root, val)  # 递归调用
                self.insert_no_rec(val)  # 非递归调用

    def insert(self, node: BiTreeNode, val: int):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.left = self.insert(node.left, val)
            node.left.parent = node
        elif val > node.data:
            node.right = self.insert(node.right, val)
            node.right.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.left:
                    p = p.left
                else:
                    p.left = BiTreeNode(val)
                    p.left.parent = p
                    return
            elif val > p.data:
                if p.right:
                    p = p.right
                else:
                    p.right = BiTreeNode(val)
                    p.right.parent = p
                    return
            else:
                return

    def query(self, node, val):
        if not node:
            return None
        else:
            if val < node.data:
                return self.query(node.left, val)
            elif val > node.data:
                return self.query(node.right, val)
            else:
                return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if val < p.data:
                p = p.left
            elif val > p.data:
                p = p.right
            else:
                return p
        return None

    def pre_order(self, tree_node: BiTreeNode):
        if tree_node:
            print(tree_node.data, end=',')
            self.pre_order(tree_node.left)
            self.pre_order(tree_node.right)

    def in_order(self, tree_node: BiTreeNode):
        """
        二叉搜索树的中序遍历一定是从小到大的
        """
        if tree_node:
            self.in_order(tree_node.left)
            print(tree_node.data, end=',')
            self.in_order(tree_node.right)

    def __remove_node_1(self, node):
        # Condition 1: 被删除的 node 是叶子节点
        if not node.parent:  # 判断是不是根结点
            self.root = None
        if node == node.parent.left:  # node 是它父亲的左子节点
            node.parent.left = None
        else:
            node.parent.right = None

    def __remove_node_21(self, node):
        # Condition 2.1: node 只有一个左子节点
        if not node.parent:
            self.root = node.left
            node.left.parent = None
        elif node == node.parent.left:
            node.parent.left = node.left
            node.left.parent = node.parent
        else:
            node.parent.right = node.left
            node.left.parent = node.parent

    def __remove_node_22(self, node):
        # Condition 2.2: node 只有一个右子节点
        if not node.parent:
            self.root = node.right
            node.right.parent = None
        elif node == node.parent.left:
            node.parent.left = node.right
            node.right.parent = node.parent
        else:
            node.parent.right = node.right
            node.right.parent = node.parent

    def delete(self, val):
        if self.root:  # 判断是不是空树
            node = self.query_no_rec(val)
            if not node:
                return False
            # 判断节点的子节点样子
            if not node.left and not node.right:
                self.__remove_node_1(node)
            elif not node.right:
                self.__remove_node_21(node)
            elif not node.left:
                self.__remove_node_22(node)
            else:
                min_node = node.right
                while min_node.left:
                    min_node = min_node.left
                # 只需要把被删除节点的 val 被替换为其右子树内的最小值
                node.data = min_node.data
                # 删除 min_node
                if min_node.right:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)




tree = BST([4, 6, 7, 9, 2, 1, 3, 5, 8])
tree.in_order(tree.root)
print()
tree.delete(4)
tree.delete(1)
tree.in_order(tree.root)
