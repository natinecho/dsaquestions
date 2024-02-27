# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hash={}
        temp=headA
        while temp:
            hash[temp]=temp.next
            temp=temp.next
            
        res=headB
        while res:
            if res in hash:
                return res
            res=res.next
        return None