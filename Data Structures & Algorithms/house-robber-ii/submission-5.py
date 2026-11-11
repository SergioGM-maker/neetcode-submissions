class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<4:
            return max(nums)
        if len(nums) == 4:
            return max(nums[0]+nums[2],nums[1]+nums[3])
    
        def robbing(numbers):
            if len(numbers) == 3:
                return max(numbers[0]+numbers[2],numbers[1])
            
            sol = [0]*len(numbers)
            sol[0] = numbers[0]
            sol[1] = numbers[1]
            sol[2] = numbers[2] + numbers[0]
            cur = 3

            while cur < len(numbers):
                sol[cur] = max(sol[cur-2],sol[cur-3]) + numbers[cur]
                cur += 1
            
            return max(sol[cur-1],sol[cur-2])

        


        return max(robbing(nums[1 :]), robbing(nums[:-1]))
        
        