#Given the head of a singly linked list, return the middle node of the linked list.

#If there are two middle nodes, return the second middle node.

#------SOLUTION----
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    # Approach - While slow moves one step forward, fast moves two steps forward.Finally, when fast reaches the end, slow happens to be in the middle of the linked list.

    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow