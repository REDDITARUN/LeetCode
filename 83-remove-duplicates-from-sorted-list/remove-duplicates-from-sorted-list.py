
class Solution(object):
    def deleteDuplicates(self, head):
        current_node = head

        while current_node and current_node.next:
            if current_node.val == current_node.next.val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
            
        
        return head




        