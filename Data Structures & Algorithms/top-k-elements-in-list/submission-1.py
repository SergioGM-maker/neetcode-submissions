class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for n in nums:
            d.update({n : d.get(n,0) + 1})
        
        ord = sorted(d.items() , key= lambda x: (-x[1],x[0]))
        
        final_list = [x[0] for x in ord]

        return final_list[:k]

        