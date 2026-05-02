class Solution {
    public int[] twoSum(int[] nums, int target) {
        int a=0;
        int b = 1;
        int test = nums[a]+nums[b];
        while(nums[a]+nums[b]!=target && a<nums.length-1){
            if(b<nums.length-1){
                b++;
            }else{
                a++;
                b=a+1;
            }
            test = nums[a]+nums[b];
        }
        int[] sol = {a,b};
        return  sol;
    }
}
