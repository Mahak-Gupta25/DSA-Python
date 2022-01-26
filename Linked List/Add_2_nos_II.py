#You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.


#Solution---
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = str2 = ''
        while l1:
            str1 += str(l1.val)
            l1 = l1.next
            
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
            
        ans = str(int(str1)+int(str2))
        
        dummy = ListNode()
        prev = dummy
        for i in ans:
            node = ListNode(int(i))
            prev.next = node
            prev = prev.next
            
        return dummy.next