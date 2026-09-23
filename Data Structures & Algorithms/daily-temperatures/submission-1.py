class Solution:




    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0 for x in temperatures]
        stack = []
        x = 0
        while x < len(temperatures):
            while stack != [] and stack[-1][0] < temperatures[x]:
                sol[stack[-1][1]] = x - stack[-1][1]
                stack.pop()
            stack.append((temperatures[x],x))
            x += 1

        return sol