# Binary Tree Level Order Traversal

# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        nodes = [root]

        index = 0
        sussesors = 1
        result = []

        while True:
            childs = 0
            level = []
            for i in range(index, index + sussesors):
                if nodes[i]:
                    level.append(nodes[i].val)
                    nodes.append(nodes[i].left)
                    nodes.append(nodes[i].right)
                    childs += 2
            if childs == 0:
                break

            result.append(level)
            index += sussesors
            sussesors = childs
        return result
