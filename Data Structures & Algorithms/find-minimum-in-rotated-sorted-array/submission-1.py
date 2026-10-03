class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        middle = int((left+right)/2)
        
        if nums[left] < nums[right]:
            return nums[left]

        while left<right-1:
            if nums[middle] > nums[left]:
                left = middle
            else:
                right = middle
            middle = int((left+right)/2)
            
        print(left)
        print(right)
        return nums[right]
        