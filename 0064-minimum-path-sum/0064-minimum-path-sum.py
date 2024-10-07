class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        di = [(0,1),(1,0)]
        dp = [[float("inf")]*m for i in range(n)]
        dp[n-1][m -1] = grid[n-1][m -1] 
        
        def bound(i,j):
            return 0 <= i< n and 0 <= j < m

        for i in range(n-1, -1,-1):
            for j in range(m - 1,-1,-1):
                temp = float("inf")
    
                for r,c in di:
                    if bound(i + r, j + c):
                        temp = min(temp,dp[i + r][j + c])
                
                if temp != float("inf"):
                    dp[i][j] = temp + grid[i][j] 
                else:
                    dp[i][j] = grid[i][j] 

        return dp[0][0]
        

        
        

        