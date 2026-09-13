class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        reference = {}
        n = 0
        while n < len(numbers):
            if reference.get(target-numbers[n]) == None:
                reference.update({numbers[n]:n})
                n=n+1
            else:
                return [reference.get(target-numbers[n]) + 1 , n + 1]
        
        return False