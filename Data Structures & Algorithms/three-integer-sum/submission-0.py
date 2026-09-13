class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        frecuency = {}
        sol = []
        for x in nums:
            if frecuency.get(x) == None:
                frecuency.update({x:1})
            else:
                frecuency.update({x:frecuency.get(x)+1})
        i = 0
        while i < len(nums):
            frecuency.update({nums[i]:frecuency.get(nums[i])-1})
            j = i+1
            while j < len(nums):
                frecuency.update({nums[j]:frecuency.get(nums[j])-1})
                lookUp = frecuency.get(-(nums[i]+nums[j]))
                if lookUp != None and lookUp>0:
                    curr = [nums[i],nums[j],-(nums[i]+nums[j])]
                    curr.sort()
                    if sol.count(curr) == 0:
                        sol.append(curr)
                frecuency.update({nums[j]:frecuency.get(nums[j])+1})
                j= j+1
            frecuency.update({nums[i]:frecuency.get(nums[i])+1})
            i=i+1
        
        return sol