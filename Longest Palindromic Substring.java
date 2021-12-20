class Solution {
    public String longestPalindrome(String s) 
    {
        int start=0,end=0;
        int length;
        for(int i=0;i<s.length();i++)
        {
            /*(s,i,i) =(string,centre of substring,centre of substring) in case of even string there are two centres i  and i+1 */
            int oddSubstringLength  =expand(s,i,i);
            int evenSubstringLength =expand(s,i,i+1);
            /*Length of substring, if even length palindrome found it will store its length and vice versa, whichever is  greater */
            length = Math.max(oddSubstringLength,evenSubstringLength);   
            
            /*If a new substring is found or found with greater length,v need to find its start and end positions in order to return the string*/
            //Substring length formula if indices are given = end-start+1
            if(length>end-start+1)
            {
                //Even len (6)-> 2    start --> i-2, end -> i+3
                //Odd len (5) -> 2    start i-2, end -> i+2
                start = i-(length-1)/2;
                end=i+length/2;
            }
        }    
            return s.substring(start,end+1);//+1 coz of java substring syntax
        
    }
    int expand(String s, int left, int right)
    {
        while(left>=0 && right<s.length() &&s.charAt(left)==s.charAt(right))
        {
            left--;
            right++;
        }
        int len = right-left-1;//length of found palindromic string
        //-1 coz the indices will be shifted one step ahead in the loop
        return len;
    }
 
}
