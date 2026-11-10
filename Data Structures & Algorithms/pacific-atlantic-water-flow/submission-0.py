class Solution:

    def BFS(self, wetLand, sea, ground):
        around = [(1,0),(-1,0),(0,1),(0,-1)]
        queue = deque(wetLand)

        while queue:
            i, j = queue.popleft()

            sea[i][j] = True
            for a,b in around:
                x = a + i
                y = b + j
                if x>=0 and y>=0 and x<len(sea) and y<len(sea[0]) and sea[x][y] != True and ground[i][j] <= ground[x][y]:
                    queue.append((x,y))

            



    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        columns = len(heights[0])
        pacific = [[False] * columns for x in range(rows)]
        atlantic = [[False] * columns for x in range(rows)]

        coastP = []
        coastA = []

        for x in range(rows):
            coastP.append((x,0))
            coastA.append((x,columns-1))
        
        for x in range(columns):
            coastP.append((0,x))
            coastA.append((rows-1,x))

        self.BFS(coastP, pacific, heights)
        self.BFS(coastA, atlantic, heights)

        sol = []

        for i in range(rows):
            for j in range(columns):
                if pacific[i][j] and atlantic[i][j]:
                    sol.append([i,j]) 

        return sol

            


        