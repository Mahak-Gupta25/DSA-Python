#Given the head of a singly linked list, return true if it is a palindrome.

#Approach 1 - find middle of linked list, reverse ll from middle till end and then traverse simultaneously while comparing the values of each nodes from start and mid.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from turtle import right


class Solution: #TC= O(n), SC= O(1)
    def isPalindrome(self, head) -> bool:
        slow = head #find mid of ll
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        prev = None # reverse from mid to last
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        left, right = head, prev # comapre values
        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
            
        return True
        

#Approach 2 - Traverse through all nodes of ll and store their values in an array. Then comapre the values from first and last of array using 2 pointers

class Solution: # TC = O(n) SC= O(n)
    def isPalindrome(self, head) -> bool:
        arr = [] # store vals in array
        while head:
            arr.append(head.val)
            head = head.next

        
        first, last = 0, len(arr)-1 # compare values
        while first <= last:
            if arr[first] != arr[last]:
                return False
            first = first +1
            last = last-1


        return True