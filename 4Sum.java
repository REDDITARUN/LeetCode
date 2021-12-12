class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        // In Four Sum, we are fixing one variable i.e. 'a' and another variable 'b', then search for 'c' & 'd' using two pointer approach
            //such that a+b+c+d==target
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        for(int i = 0; i<nums.length-3; i++){
            int a = nums[i]; // here we are fixing a 
            if(i>0 && nums[i] == nums[i-1]){
                continue;
            }
            for(int j = i+1; j<nums.length-2; j++){
                if(j>i+1 && nums[j] == nums[j-1]){
                continue;
                }
                int b = nums[j]; //here we are fixing b
                // now taking the b as support we use two ponter approach
                // start and end will be c and d
                int start = j+1, end = nums.length-1;
                while(start < end){
                    int sum = a+b+nums[start]+nums[end];
                    if(sum == target){
						result.add(Arrays.asList(a,b,nums[start],nums[end]));
                        while(start < end && nums[start] == nums[start+1]){
                            start++;
                        }
                        while(start < end && nums[end] == nums[end-1]){
                            end--;
                        }
                        start++;
                        end--;
                    }else if(sum<target){
                        start++;
                    }else{
                        end--;
                    }
                }
            }
        }
        return result;
        
    }
}



    
