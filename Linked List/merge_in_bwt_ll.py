#You are given two linked lists: list1 and list2 of sizes n and m respectively.

#Remove list1's nodes from the ath node to the bth node, and put list2 in their place.


#SOLUTION
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        curr_a, curr_b = list1, list1
        
        while a-1:
            curr_a = curr_a.next
            a -=1
            
        while b+1:
            curr_b = curr_b.next
            b -=1
            
        curr_a.next = list2
        while list2.next:
            list2 = list2.next
            
        list2.next = curr_b
        
        return list1
            