# Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr_node = head
        while curr_node.next:
            next = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next
        return curr_node
