class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def recurs(i: int, curr: List[int], accumulation):
            if accumulation == target:
                res.append(curr.copy())
                return
            elif accumulation > target or i == len(candidates):
                return
            
            curr.append(candidates[i])
            recurs(i +1, curr, accumulation + candidates[i])
            curr.pop()
            
            while i<len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1 
            recurs(i + 1, curr, accumulation)

        recurs(0,[],0)
        return res