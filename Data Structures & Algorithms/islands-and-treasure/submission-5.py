class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return None
        
        i = 0
        n = len(grid)
        j = 0
        m = len(grid[0])
        queue = deque()

        # Introducing in the queue the initial components

        while i < n:
            while j < m:

                if grid[i][j] == 0:
                    queue.append([i,j,0])
                j+=1
            j=0
            i+=1
        
        # Filling the cells using a breadth first approach

        while queue: 
            ix, jx, val = queue.popleft()
            
            if grid[ix][jx] < val: # cell already filled by a lower value
                continue

            for iy, jy in [(ix-1,jx),(ix+1,jx),(ix,jx-1),(ix,jx+1)]:
                if iy >= 0 and jy >= 0 and iy < n and jy < m and grid[iy][jy] == 2147483647: # illegal cells avoided, only infs filled
                    grid[iy][jy] = grid[ix][jx] +1
                    queue.append([iy,jy,val+1])

