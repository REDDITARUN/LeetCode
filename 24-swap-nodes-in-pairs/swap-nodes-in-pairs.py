# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            current.next = second
            first.next = second.next
            second.next = first

            current = first
        
        return dummy.next

        
        while head:
            temp = head
            if head.next:
                head = head.next
                head.next = temp

            if head.next.next:
                head = head.next.next
        return head

        