# Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.
#
# A binary tree's maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def rec_func(node: TreeNode) -> int:
                if not node:
                    return 0
                if not node.left and not node.right:
                    return 1
                return max(rec_func(node.left), rec_func(node.right)) + 1
        return rec_func(root)
