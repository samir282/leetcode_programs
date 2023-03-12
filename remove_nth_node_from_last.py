# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # nth node removal from start
        '''new_node=head
        for i in range(n-2):
            new_node=new_node.next
        
        if new_node.next:
            new_node.next=new_node.next.next
        else:
            new_node.next=None
        print(head)
        return head'''
        
        
        fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
