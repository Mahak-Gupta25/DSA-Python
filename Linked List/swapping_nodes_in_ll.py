#You are given the head of a linked list, and an integer k.
#Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).


#SOLUTION 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head, k: int):
        if not head:
            return None
        
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        
        
        reverse_k = length-k+1 #define reverse_k here because k will change value after first loop
        
        begin_node = head
        while k-1:
            begin_node =  begin_node.next
            k -=1
       
        
        end_node = head
        while reverse_k-1:
            end_node = end_node.next
            reverse_k -= 1
     
            
        begin_node.val, end_node.val = end_node.val, begin_node.val
        
        return head
            