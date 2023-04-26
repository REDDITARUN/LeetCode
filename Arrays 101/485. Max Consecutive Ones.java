class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int rep = 0;
        int count = 0;

        for (int i = 0; i < nums.length; i++)
        {
            if (nums[i] == 1)
            {
                count ++;
            }
            else
            {
                rep = Math.max(rep, count);
                count = 0;
            }
        }
        return Math.max(rep, count);
    }
}