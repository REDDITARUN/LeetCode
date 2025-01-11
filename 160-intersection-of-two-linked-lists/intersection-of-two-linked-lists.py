# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if not headA or not headB:
            return None


        top_pointer = headA
        bottom_pointer = headB

        while top_pointer!= bottom_pointer:
            if top_pointer:
                top_pointer = top_pointer.next
            else:
                top_pointer = headB
            if bottom_pointer:
                bottom_pointer = bottom_pointer.next
            else:
                bottom_pointer = headA
        return top_pointer


        