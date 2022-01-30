#Given the head of a linked list, rotate the list to the right by k places.


#SOLUTION
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):
        if not head:
            return None
        
        tail = head
        count = 1
        while tail.next: 
            tail = tail.next
            count+=1
       
        k = k%count
        curr = head
        x = count-1-k
        while x:
            curr = curr.next
            x -=1
        
        tail.next = head
        head = curr.next
        curr.next = None
        
        return head