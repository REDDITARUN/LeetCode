# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy_list = ListNode()
        start_point = dummy_list

        while list1 and list2:
            if list1.val < list2.val:
                start_point.next = list1
                list1 = list1.next
            else:
                start_point.next = list2
                list2 = list2.next

            start_point = start_point.next

        if list1:
            start_point.next = list1
        elif list2:
            start_point.next = list2

        

        return dummy_list.next

        
        
        
        
        