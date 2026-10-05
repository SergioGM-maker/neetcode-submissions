class Solution:
    def search(self, nums: List[int], target: int) -> int:

        mid = self.findMin(nums)
        ordered = []
        
        op1 = nums[mid:len(nums)]
        op2 = nums[0:mid]
        if mid <= 1 and (op2 == [] or op2[0]<op1[0]):
            return self.binarySearch(nums,target)
        
        if target <= op1[-1] and target >= op1[0]:
            sol = self.binarySearch(op1,target)

            if sol == -1:
                return -1
            else:
                return sol + mid

        elif target <= op2[-1] and target >= op2[0]:
            return self.binarySearch(op2,target)
        return -1
        

    def binarySearch(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        middle = (left+right)//2
        while left <= right:
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle-1
            middle = (left+right)//2

        return -1


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
        return right
        