# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        temp=head
        sml_head=sml=ListNode()
        lrg_head=lrg=ListNode()

        while temp:
            if temp.val>=x:
                lrg.next=temp
                lrg=lrg.next
            else:
                sml.next=temp
                sml=sml.next
            temp=temp.next
        lrg.next=None
        sml.next=lrg_head.next

        return sml_head.next
        