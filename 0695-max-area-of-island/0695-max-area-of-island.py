class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        di = [(1,0),(-1,0),(0,1),(0,-1)]
        def bound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        maxx = 0
        visited = set()
        def dfs(row,col):
            temp = 1

            for r,c in di:
                nr = row + r
                nc = col + c
                if bound(nr,nc) and (nr,nc) not in visited and grid[nr][nc] == 1:
                    visited.add((nr,nc))
                    temp += dfs(nr,nc)

            return temp
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    visited.add((i,j))
                    maxx = max(maxx,dfs(i,j))

        return maxx

        