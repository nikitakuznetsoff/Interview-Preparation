# Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next == None:
            return None

        first_counter = head
        second_counter = head

        for i in range(n-1):
            first_counter = first_counter.next

        prev = None
        while first_counter.next:
            first_counter = first_counter.next
            prev = second_counter
            second_counter = second_counter.next

        if second_counter.next == None:
            prev.next = None
            return head

        while second_counter.next:
            second_counter.val = second_counter.next.val
            prev = second_counter
            second_counter = second_counter.next
        prev.next = None

        return head
