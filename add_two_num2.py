# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def retrive_number(list: Optional[ListNode]) -> int:
        num = 0
        if list is not None:
            Solution.retrive_number(list.next)
            return num*10+list.val
            
        

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = Solution.retrive_number(l1)
        num2 = Solution.retrive_number(l2)
        final_num = num1+num2
        print(final_num)
        return l1