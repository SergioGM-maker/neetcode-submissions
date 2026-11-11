class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 2
        
        sol = [0]*(n)
        sol[0] = 1
        sol[1] = 2
        cur = 2
        while sol[n-1] == 0:
            sol[cur] = sol[cur-1] + sol[cur-2] 
            cur += 1
        print(sol)
        return sol[n-1]
        