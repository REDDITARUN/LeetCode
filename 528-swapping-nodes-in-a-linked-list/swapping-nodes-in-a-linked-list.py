# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        current = head
        len = 0
        while current:
            len += 1
            current = current.next
        
        if len < k:
            return head
        
        initial_k = final_k = head

        for _ in range(k-1):
            initial_k = initial_k.next

        for _ in range(len - k):
            final_k = final_k.next
        
        initial_k.val, final_k.val = final_k.val, initial_k.val

        return head
        