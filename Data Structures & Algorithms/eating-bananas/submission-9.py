class Solution:

    def test_bananas_eaten_on_time(self,middle: int,piles: List[int],h: int) -> bool:
        hours = 0
        curr = 0
        division = 0
        while piles[-1] > 0:
            division = (piles[curr]+middle-1)//middle
            piles[curr] = 0
            hours += division
            curr += 1

            if hours > h:
                return False
                
        return True
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]
        middle = int((left+right)/2)
        best = right
        while left <= right:
            check = self.test_bananas_eaten_on_time(middle,piles.copy(),h)

            if check is False:
                left = middle+1
            else:
                best = middle
                right = middle-1

            middle = int((left+right)/2)
        return best