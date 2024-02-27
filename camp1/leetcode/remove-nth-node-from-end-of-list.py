# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        if count==0:
            return None

        num=count-n-1
        res=head
        for i in range(num):
            res=res.next
        if num>=0:
            res.next=res.next.next
        else:
           return head.next

        return head
        