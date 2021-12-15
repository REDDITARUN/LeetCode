/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) 
    {
        ListNode result = new ListNode(0); // this is the final node where we store the result
        ListNode curr = result; //Pointer initially at temp
        int carry = 0; // carry for addition
        
        while(l1 != null ||  l2 != null || carry ==1) //run the loop until one of then goes to null
            
        {
            int sum = 0;
            if(l1 != null)
            {
                sum += l1.val;
                l1= l1.next;
            }
            if(l2 != null)
            {
                sum += l2.val;
                l2 = l2.next;
            }
            // here sum adapts the value of l1 then l2 
            sum += carry; //add carry to the sum
            carry = sum/10;
            ListNode node = new ListNode(sum % 10); // store the sum leaving the carry
            curr.next = node;
            curr =curr.next;
            
        }
        return result.next;
        
    }
}
