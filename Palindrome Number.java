
class Solution {
    public boolean isPalindrome(int x) 
    {
        int n = x;
      
        if(x<0) // For negative numbers it will return false
        {
            return false;
        }
        int p = 0;
        while(x>0)
        {
            p = p * 10 + (x%10);
            x /= 10;
            
        }
        return p == n;
        
        
        
        
    }
}
