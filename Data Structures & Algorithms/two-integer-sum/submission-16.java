class Solution {
    public int[] twoSum(int[] nums, int target) {
        int a=0;
        int b=1;
        for (int i = 0; i<nums.length-1; i++){
            for(int j = i+1; j<nums.length; j++){
                if(target==nums[i]+nums[j]){
                    a=i;
                    b=j;
                }
            }
        }
        int[] sol = {a,b};
        return sol;
    }
}
