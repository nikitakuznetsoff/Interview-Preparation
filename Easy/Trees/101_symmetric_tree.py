# Symmetric Tree

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        nodes = [root]
        nodes.append(root.left)
        nodes.append(root.right)

        index = 1
        sussesors = 2

        while True:
            # Checking
            for i in range(int(sussesors/2)):
                left_index = index + i
                right_index = index + sussesors - 1 - i
                if not nodes[left_index] and not nodes[right_index]:
                    continue
                if not nodes[left_index] or not nodes[right_index]:
                    return False
                if nodes[left_index].val != nodes[right_index].val:
                    return False
            childrens = 0
            # Insertings sussesors
            for i in range(index, index+sussesors):
                if nodes[i]:
                    nodes.append(nodes[i].left)
                    nodes.append(nodes[i].right)
                    childrens += 2

            if childrens == 0:
                break
            index += sussesors
            sussesors = childrens
        return True
