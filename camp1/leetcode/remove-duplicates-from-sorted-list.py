# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list1=head
        list2=head
        if not head:
            return None
        while list1:
            if list1.val==list2.val:
                list1=list1.next
                continue
            list2.next=list1
            list2=list2.next
            list1=list1.next
        list2.next=None
        return head

            


        

        