class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost or len(cost)<2:
            return 0
        
        accumulated = [0]*len(cost)
        
        accumulated[0] = cost[0]
        accumulated[1] = cost[1]
        cur = 2
        while cur < len(cost):
            accumulated[cur] = min(accumulated[cur-1],accumulated[cur-2]) + cost[cur]
            
            cur += 1

        return min(accumulated[cur-1],accumulated[cur-2])