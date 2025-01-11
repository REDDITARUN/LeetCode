# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        res = 0
        curr = head

        while curr is not None:
            res = 2 * res + curr.val
            curr = curr.next
        return res

        