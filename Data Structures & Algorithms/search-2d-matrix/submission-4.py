class Solution:
    def search(self, nums: List[int], target: int) -> bool:
            left = 0
            right = len(nums) -1
            middle = left+(right-left)//2
            while left <= right:
                curr = nums[middle]
                if curr == target:
                    return True
                elif curr < target:
                    left= middle+1
                    middle = left + (right-left)//2
                else:
                    right= middle-1
                    middle = left + (right-left)//2
            return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        

        row = 0
        while row < len(matrix):
            
            if matrix[row][-1] >= target and matrix[row][0] <= target:
                return self.search(matrix[row],target)
                
            
            if matrix[row][0] > target and matrix[row][-1] > target:
                return False

            row += 1 


        return False