class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        a = 0
        while len(stones)>1:
            print(stones[0])
            a = -heapq.heappop(stones)
            a += heapq.heappop(stones)
            
            if a>0:
                heapq.heappush(stones, -a)



        if len(stones) == 0:
            return 0
        else:
            return -stones[0]
        