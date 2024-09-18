class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:

        dp = [-1]*len(grid)

        for  i in range(len(grid)):
            dp[i] = 0

        di = [(-1,-1),(0,-1),(1,-1)]

        def bound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        for i in range(1,len(grid[0])):
            curr  = [-1] * len(grid)
            for j in range(len(grid)):
                maxx = -1
                for r,c in di:
                    nr,nc = j + r,i + c
                    if bound(nr,nc) and grid[j][i] > grid[nr][nc] and dp[nr] != -1:
                        maxx = max(maxx,dp[nr] + 1)

                # print("here",grid[j][i],i,j,maxx)
                curr[j] = maxx

            # print(curr,dp)
            if max(curr) == -1:
                return max(0,max(dp)) 
            dp = curr[::]


        return max(dp)

        