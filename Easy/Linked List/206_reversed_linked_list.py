# Reverse Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr_node = head
        while curr_node.next:
            next = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next
        curr_node.next = prev
        return curr_node


head = ListNode(val=1)
prev = head
for i in range(2, 6):
    node = ListNode(val=i)
    prev.next = node
    prev = node

v = Solution().reverseList(head)
while v.next:
    print(v.val)
    v = v.next
print(v.val)