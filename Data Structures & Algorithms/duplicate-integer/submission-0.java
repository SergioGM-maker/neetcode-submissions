class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean sol= false;
        int curr =0;
        int[] sub = {};
        for(int x: nums){
            curr++;
            sub = Arrays.copyOfRange(nums,curr,nums.length);
            for(int y: sub){
                if(x==y){
                    sol=true;
                    break;
                }
            }
            if(sol==true || curr==nums.length){
                break;
            }
        }


        return sol;
    }
}