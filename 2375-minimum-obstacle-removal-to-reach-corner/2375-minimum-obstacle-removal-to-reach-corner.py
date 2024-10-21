class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        di = [(0,1),(1,0),(-1,0),(0,-1)]

        def bound(i , j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        heap = [(0,0,0)]
        visited = set()


        while heap:
            obs,row,col = heappop(heap)

            if row == len(grid) -1 and col == len(grid[0]) -1:
                return obs

            if (row,col) not in visited:
                visited.add((row,col))

                for r,c in di:
                    nr, nc = row + r, col + c

                    if bound(nr,nc) and (nr,nc) not in visited:
                        temp = obs + 1 if grid[nr][nc] == 1 else obs
                        heappush(heap,(temp,nr,nc))


        
        return -1


        
        