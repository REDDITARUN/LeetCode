# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        stack = []
        current = head

        while current:

            while stack and stack[-1].val < current.val:
                stack.pop()

            stack.append(current)
            current = current.next

        dummy = ListNode(0)

        tail = dummy

        for node in stack:
            tail.next = ListNode(node.val)
            tail = tail.next
        
        tail.next = None
        return dummy.next