#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# EXAMPLE-------
#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.


#Approach -- Store the values in a strings and then add final string values. Convert the ffinal answer into ll

#SOLUTION ---

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        str1 = ''
        str2 = ''
        while l1:
            str1 += str(l1.val)
            l1 = l1.next
            
        while l2:
            str2 += str(l2.val)
            l2 = l2.next
            
        ans = int(str1[::-1]) + int(str2[::-1])
        
        
        answer = str(ans)[: :-1]
        
        
        dummy = ListNode()
        prev = dummy
        for i in answer:
            node = ListNode(int(i))
            prev.next = node
            prev = prev.next
            
        return dummy.next