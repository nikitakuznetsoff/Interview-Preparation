# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return None

        turtle = head
        hare = head

        if head:
            if head.next:
                hare = head.next.next
            else:
                return False


        while turtle:
            if turtle == hare:
                return True
            turtle = turtle.next
            if hare:
                if hare.next:
                    hare = hare.next.next
                else:
                    hare = hare.next
        return False


        
        s = set()
        node = head
        while node.next:
            if node in s:
                return True
            s.add(node)
            node = node.next
        return False