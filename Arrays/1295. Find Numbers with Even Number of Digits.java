class Solution {
    public int findNumbers(int[] nums) {
         int count = 0;
         int total = 0;

        for (int i = 0; i < nums.length; i++)
        {
            while (nums[i] != 0)
            {
                nums[i] /= 10;
                ++count;
            }
            if(count % 2 == 0)
            {
                ++total;
            }
            count = 0;

        }
        return total;
        
    }
}