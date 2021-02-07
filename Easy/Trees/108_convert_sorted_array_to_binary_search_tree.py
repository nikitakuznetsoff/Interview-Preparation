# Convert Sorted Array to Binary Search Tree

# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def binary_tree_rec(left: int, right: int) -> TreeNode:
            if right - left < 0:
                return

            if right - left == 0:
                return TreeNode(val=nums[left])

            if right - left = 1:
                node = TreeNode(val=nums[left])
                return TreeNode(val=nums[right], left=node)

            middle = (left + right) / 2
            left_node = sortedArrayToBST(left, middle-1)
            right_node = sortedArrayToBST(middle+1, right)
            return TreeNode(val=nums[middle], left=left_node, right=right_node)
        return binary_tree_rec(0, len(nums)-1)
