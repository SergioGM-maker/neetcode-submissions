class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [[(x[0]**2)+(x[1]**2),x[0],x[1]] for x in points]
        heapq.heapify(heap)
        
        sol = []
        while k>0:
            k -= 1
            dist, x, y = heapq.heappop(heap)
            sol.append([x,y])
        return sol