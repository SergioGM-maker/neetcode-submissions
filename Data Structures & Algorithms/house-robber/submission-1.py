class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        if len(nums) == 3:
            return max(nums[0]+nums[2],nums[1])

        sol = [0]*len(nums)
        sol[0] = nums[0]
        sol[1] = nums[1]
        sol[2] = nums[2] + nums[0]
        cur = 3
        while cur < len(nums):
            sol[cur] = max(sol[cur-2],sol[cur-3]) + nums[cur]
            cur += 1
        
        return max(sol[cur-1],sol[cur-2])