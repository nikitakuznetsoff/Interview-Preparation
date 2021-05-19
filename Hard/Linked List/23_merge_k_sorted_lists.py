  # Definition for singly-linked list.

from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        def merge(left: ListNode, right: ListNode) -> ListNode:
            if not left:
                return right
            if not right:
                return left
            if not right and not left:
                return None
            head = ListNode()
            node = head
            while left or right:
                if not left:
                    node.val = right.val
                    right = right.next
                elif not right:
                    node.val = left.val
                    left = left.next
                else:
                    if left.val < right.val:
                        node.val = left.val
                        left = left.next
                    else:
                        node.val = right.val
                        right = right.next
                if left or right:        
                    next_node = ListNode()
                    node.next = next_node
                    node = next_node
            return head

        curr_length = len(lists)
        while curr_length > 1:
            indx = 0
            counter = 0
            for i in range(1, curr_length, 2):
                mrg = merge(lists[i], lists[i-1])
                if mrg:
                    lists[indx] = mrg
                    indx += 1
                else:
                  counter += 2
            
            if curr_length % 2 == 1:
                lists[indx] = lists[curr_length-1]

            curr_length -= counter
            curr_length = int(curr_length  / 2) + curr_length % 2
        return lists[0]