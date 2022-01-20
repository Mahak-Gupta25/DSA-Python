#Given the head of a singly linked list, reverse the list, and return the reversed list.

#----SOLUTION-----

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        return prev
        #(Time complexity = O(n), Space complexity = O(1))

#Recursive Solution-

class Solution:
    def reverseList(self, head):
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead