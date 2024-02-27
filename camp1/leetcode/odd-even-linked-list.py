# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        even_head =even= ListNode()
        odd_head =odd=  ListNode()

        # even_head = ListNode()
        # odd_head =  ListNode()
        # odd = ListNode()
        # even = ListNode()
        # even_head.next=even
        # odd_head.next=odd

        f=1
        while temp:
            if f==1:
                even.next=temp
                even=even.next
                f=0
            else:

                odd.next=temp
                odd=odd.next
                f=1
            temp=temp.next

        odd.next=None 
        even.next=odd_head.next
        return even_head.next
        # even.next=odd_head.next.next
        # return even_head.next.next