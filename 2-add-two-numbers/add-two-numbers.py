# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current = dummy
        carry = 0 

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            value = val1 + val2 + carry
            carry = value // 10
            new_val = value % 10

            current.next = ListNode(new_val)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return dummy.next
        