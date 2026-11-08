class Solution:

    def wreck(self, grid: List[List[str]], i: int, j: int):
        if (
            i < len(grid) and i >= 0 and 
            j < len(grid[0]) and j >= 0 
            and grid[i][j] == "1"):
            
            grid[i][j] = "0"
            self.wreck(grid,i-1,j)
            self.wreck(grid,i+1,j)
            self.wreck(grid,i,j-1)
            self.wreck(grid,i,j+1)
        

        return grid

    def numIslands(self, grid: List[List[str]]) -> int:
        i, j = 0 , 0
        count = 0

        while i < len(grid):
            while j < len(grid[0]):
                if grid[i][j] == "1":
                    count += 1
                    self.wreck(grid, i, j)
                j += 1
            j = 0
            i += 1

 
        return count
        