class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return None

        i = 0
        n = len(grid)
        j = 0
        m = len(grid[0])
        this_round = deque()
        next_round = deque()
        remainingFruit = 0

        # counting fruits and queing the fruits about to rot
        while i < n:
            while j < m:
                
                if grid[i][j] == 1:
                    remainingFruit += 1 # counting

                if grid[i][j] == 2:
                    for ix, jx in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                        if ix >= 0 and jx >= 0 and ix < n and jx < m and grid[ix][jx] == 1:
                            this_round.append((ix,jx))  # Adding the fruits in inmediate danger
                j += 1
            j = 0
            i += 1
        
        minute = 0
        # We proccess the grid until no healthy fruit remains or there are no nodes to proccess
        while remainingFruit > 0 and (this_round or next_round):
            minute += 1
            while this_round:
                ic, jc = this_round.popleft()

                if grid[ic][jc] == 2:
                    continue # we skip repeated nodes

                grid[ic][jc] = 2
                remainingFruit -= 1

                for ix, jx in [(ic-1,jc),(ic+1,jc),(ic,jc-1),(ic,jc+1)]:
                        if ix >= 0 and jx >= 0 and ix < n and jx < m and grid[ix][jx] == 1:
                            next_round.append((ix,jx))  # Adding the new fruits in inmediate danger

            this_round = next_round
            next_round = deque()
            
        
        if remainingFruit != 0:
            return -1
        return minute