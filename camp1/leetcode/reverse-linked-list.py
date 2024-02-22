# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=[]
        res=head
        fin=head
        while head:
            temp.append(head.val)
            head=head.next
        while res:
            res.val=temp.pop()
            res=res.next
        return fin

        



        