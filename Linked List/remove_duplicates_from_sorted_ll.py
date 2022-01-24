#Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

#Solution --

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution: #TC = O(N) -> Beacuase each node is traversed only once. SC=O(1) 
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next= curr.next.next
            curr = curr.next
        return head

