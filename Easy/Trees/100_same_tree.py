# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def bfs(p, q):
            first = [p]
            second = [q]
            first_ind, second_ind = 0, 0
          
            while True:
                if not first[first_ind] and not second[second_ind]:
                    break

                if first[first_ind].val != second[second_ind].val:
                    return False
                
                if (first[first_ind].left == None) + (second[second_ind].left == None) == 1 or \
                  (first[first_ind].right == None) + (second[second_ind].right == None) == 1:
                    return False

                first.append(first[first_ind].left)
                second.append(second[second_ind].left)

                first.append(first[first_ind].right)
                second.append(second[second_ind].right)

                first_ind += 1
                second_ind += 1
            return True
        return bfs(p, q)
                        
            