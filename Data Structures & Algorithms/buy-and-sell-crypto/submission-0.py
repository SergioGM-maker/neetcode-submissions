class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        sol = 0
        lowest = prices[0]
        for elem in prices:
            if elem<lowest:
                lowest = elem
            else:
                sol = max(sol, elem-lowest)
        return sol