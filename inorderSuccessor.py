# Inorder Successor in BST
# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
# The successor of a node p is the node with the smallest key greater than p.val

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ
  
  
# Custom test case
# [2,1,3]
# 1
