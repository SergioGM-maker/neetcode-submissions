class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if not nums:
            return []
        
        i = 1
        curr_max = max(nums[0 : k])
        sol = []
        sol.append(curr_max)
        out = 0
        while i < len(nums) - k + 1:
            out = nums[i-1]
            newest = nums[i+k-1]
            if out == curr_max and newest < curr_max:
                curr_max = max(nums[i:i+k])
            elif newest >= curr_max:
                curr_max = newest
            sol.append(curr_max)
            i += 1

        return sol