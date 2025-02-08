class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]

        for i in range(len(triangle)-2,-1,-1):
            curr = triangle[i]
            for j in range(len(curr)):
                curr[j] = min(curr[j] + dp[j + 1], curr[j] + dp[j])
            dp = curr

        return dp[0]
        