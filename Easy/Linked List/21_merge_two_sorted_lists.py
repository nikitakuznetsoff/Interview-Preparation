# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        
        head = None
        left = l1
        right = l2
            
        if left.val < right.val:
            head = left
            left = left.next
        else:
            head = right
            right = right.next
            
        node = head
        while left or right:
            if not left:
                node.next = right
                right = right.next
            elif not right:
                node.next = left
                left = left.next
            else:
                if left.val < right.val:
                    node.next = left
                    left = left.next
                else:
                    node.next = right
                    right = right.next
            node = node.next
        return head