# -*- coding: utf-8 -*-
"""
@File:Basic_Data_Structure_Alogorithm_Bilibili-PyCharm-11_AVLTree.py
@Date: 18/1/2022
@Author: Yubo Sun
@E-mail: tyriongump@gmail.com
@Github: TyrionGump
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


class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0


class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):
        s2 = c.left
        p.right = s2

        if s2:  # 判断 s2 是不是空的
            s2.parent = p

        c.left = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.right
        p.left = s2

        if s2:
            s2.parent = p

        c.right = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):
        # 先右旋
        g = c.left

        s3 = g.right
        c.left = s3

        if s3:
            s3.parent = c

        g.right = c
        c.parent = g

        # 再左旋
        s2 = g.left
        p.right = s2

        if s2:
            s2.parent = p

        g.left = p
        p.parent = g

        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else:
            p.bf = 0
            c.bf = 0

        return g

    def rotate_left_right(self, p, c):
        g = c.right

        s2 = g.left
        c.right = s2

        if s2:
            s2.parent = c

        g.left = c
        c.parent = g

        s3 = g.right
        p.left = s3

        if s3:
            s3.parent = p

        g.right = p
        p.parent = g

        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0

        return g

    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.left:
                    p = p.left
                else:
                    p.left = AVLNode(val)
                    p.left.parent = p
                    node = p.left  # 存储插入的节点并进行后续旋转处理
                    break
            elif val > p.data:
                if p.right:
                    p = p.right
                else:
                    p.right = AVLNode(val)
                    p.right.parent = p
                    node = p.right
                    break
            else:
                return

        while node.parent:
            if node.parent.left == node:  # 插入到左子树
                if node.parent.bf < 0:
                    g = node.parent.parent
                    x = node.parent
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                elif node.parent.bf > 0:
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else:  # 插入到右子树
                if node.parent.bf > 0:
                    g = node.parent.parent
                    x = node.parent
                    if node.bf < 0:
                        n = self.rotate_right_left(node.parent, node)
                    else:
                        n = self.rotate_left(node.parent, node)
                elif node.parent.bf < 0:
                    node.parent.bf = 0
                    break
                else:
                    node.parent.bf = 1
                    node = node.parent
                    continue

            n.parent = g
            if g :
                if x == g.left:
                    g.left = n
                else:
                    g.right = n
                break
            else:
                self.root = n
                break

tree = AVLTree([9, 8, 7, 6, 5, 4, 3, 2, 1])

tree.pre_order(tree.root)
print()
tree.in_order(tree.root)




















