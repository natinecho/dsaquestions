# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        demo = None
        temp = None
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                if demo is None:
                    demo = list1
                    temp = list1
                else:
                    temp.next = list1
                    temp = list1
                list1 = list1.next
            else:
                if demo is None:
                    demo = list2
                    temp = list2
                else:
                    temp.next = list2
                    temp = list2
                list2 = list2.next
        
        while list1 is not None:
            if demo is None:
                demo = list1
                temp = list1
            else:
                temp.next = list1
                temp = list1
            list1 = list1.next
        
        while list2 is not None:
            if demo is None:
                demo = list2
                temp = list2
            else:
                temp.next = list2
                temp = list2
            list2 = list2.next
        
        return demo



             

