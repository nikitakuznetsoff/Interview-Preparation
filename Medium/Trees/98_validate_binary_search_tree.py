# Validate Binary Search Tree

# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#
# A valid BST is defined as follows:
#
#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# test

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def rec_func(node: TreeNode, min: int, max: int) -> bool:
            if node.val <= min or node.val >= max:
                return False
            result = True
            if node.left:
                result *= rec_func(node.left, min, node.val)
            if node.right:
                result *= rec_func(node.right, node.val, max)
            return result
        return rec_func(root, -2**31-1, 2**31+2)
