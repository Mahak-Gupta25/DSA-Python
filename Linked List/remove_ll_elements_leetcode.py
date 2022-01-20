#Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


#APPROACH-> traverse the Linked list and whenever the required value occurs update prev and current pointers


#-- SOLUTION --
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val: int):
        dummy = ListNode(next = head)
        prev = dummy
        curr = head
        
        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
                
            curr = nxt
            
        return dummy.next

# TC = O(n)
# SC = O(1) 