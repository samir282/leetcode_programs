# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        final_list = list2
        if list1.val < list2.val:
            final_list = list1
            list1 = list1.next
            final_list.next = list2
        
        curr = final_list
        while list1 is not None:
            if list1.val >= curr.val and (curr.next is None or list1.val < curr.next.val):
                temp = curr.next
                curr.next = list1
                list1 = list1.next
                curr.next.next = temp
                curr = curr.next
            else:
                curr = curr.next
                
        return final_list


