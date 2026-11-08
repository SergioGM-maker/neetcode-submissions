class Solution:
    def recArea(self, grid: List[List[int]], i: int, j:int) -> int:
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 0
        if grid[i][j] == 1:
            grid[i][j] = 0
            sol = 1 
            sol += self.recArea(grid,i,j+1)
            sol += self.recArea(grid,i,j-1)
            sol += self.recArea(grid,i+1,j)
            sol += self.recArea(grid,i-1,j)


            return sol
        return 0


    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        i = 0
        j = 0

        m = 0
        while i < len(grid):
            while j < len(grid[0]):
                if grid[i][j] == 1:
                    m = max(m,self.recArea(grid,i,j))
                j+=1
            i+=1
            j = 0
        return m