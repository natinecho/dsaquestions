class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def bound(i, j):
            return 0 <= i < len(grid1) and 0 <= j < len(grid1[0])
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def dfs(i, j):
            visited.add((i, j))
            st = [(i,j)]

            isFound = True
            
            while st:
                row,col = st.pop()

                for r, c in directions:
                    nr, nc = row + r, col + c
                    
                    if bound(nr, nc) and (nr, nc) not in visited and grid2[nr][nc] == 1:
                        if not grid1[nr][nc]:
                            isFound = False

                        visited.add((nr, nc))
                        st.append((nr,nc))
                    
            return isFound
        
        visited = set()
        ans = 0
        
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1 and (i, j) not in visited:
                    if grid1[i][j] == 1 and dfs(i, j):
                        ans += 1
        
        return ans
