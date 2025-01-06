class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        di = [(0,1),(1,0),(-1,0),(0,-1)]

        def bound(i,j):
            return 0 <= i <len(grid) and 0 <= j <len(grid[0])

        visited = set()

        def dfs(i,j):
            st = [(i,j)] 

            while st:
                r,c = st.pop()
                for nr ,nc in di:
                    row = nr + r 
                    col = nc + c 
                    if bound(row,col) and (row,col) not in visited and grid[row][col] == "1":
                        visited.add((row,col))
                        st.append((row,col))

        
        count = 0


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == "1":
                    count += 1
                    visited.add((i,j))
                    dfs(i,j)

        return count
        