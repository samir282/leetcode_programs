# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # node1 = head
        # list = []
        # while 1:
        #     if head == None:
        #         return None
        #     if head.next in list:
        #         return head.next 
        #     list.append(head)
        #     head = head.next
        # print(list)

        slow = head
        fast = head
        flag = False
        while fast != None and fast.next!=None:
            slow= slow.next
            fast = fast.next.next
            if slow==fast:
                print(fast,slow)
                flag = True
                break
        if not flag:
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head
