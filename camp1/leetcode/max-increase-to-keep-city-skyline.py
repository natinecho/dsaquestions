class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = []
        col_max = []
        ans=0
        
        for i in grid:
            row_max.append(max(i))
        
        for i in range(len(grid)):
            temp=0
            for j in range(len(grid[0])):
                temp= max(temp,grid[j][i])
            col_max.append(temp)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += (min( row_max[i] , col_max[j] ) - grid[i][j] )
                 
        print(row_max , col_max)
        return ans

        