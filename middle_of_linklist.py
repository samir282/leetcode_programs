# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        leng=0
        temp=head
        while(temp!=None):
            leng+=1
            temp=temp.next
        new_node= head
        mid= leng//2
        for i in range(mid):
            new_node= new_node.next
        return new_node 