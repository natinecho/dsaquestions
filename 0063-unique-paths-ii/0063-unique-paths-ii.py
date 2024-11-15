class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[-1][-1] == 1:
            return 0
            
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1

        def bound(i,j):
            if 0 <= i < m and 0 <= j < n:
                if obstacleGrid[i][j] == 1:
                    return 0
                return dp[i][j]
            return 0
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = max(dp[i][j] , bound(i - 1 ,j) + bound(i , j -1))

        return dp[-1][-1]
        