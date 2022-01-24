#Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.


#Solution--
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution: #TC= o(m+n), SC= O(n)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashmap = {}
        while headA:
            hashmap[headA]=1
            headA = headA.next
        
        while headB and headB not in hashmap:
            headB= headB.next
            
        return headB


