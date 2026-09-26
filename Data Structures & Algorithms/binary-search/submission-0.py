class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        middle = left+(right-left)//2
        while left <= right:
            curr = nums[middle]
            if curr == target:
                return middle
            elif curr < target:
                left= middle+1
                middle = left + (right-left)//2
            else:
                right= middle-1
                middle = left + (right-left)//2
        return -1