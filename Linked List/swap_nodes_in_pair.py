#Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)


#Solution-----

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        
        while curr and curr.next:
            nxtPair = curr.next.next
            second = curr.next
            
            second.next = curr
            curr.next = nxtPair
            prev.next = second
            
            prev = curr
            curr = nxtPair
            
        return dummy.next