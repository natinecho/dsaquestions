class Solution:
    def jump(self, nums: list[int]) -> int:

        n = len(nums)
        dp = [float("inf")]*n

        dp[-1] = 0

        for i in range (n - 2, -1, -1):
            for j in range(nums[i] + 1):
                dp[i] = min(dp[i], dp[min(n - 1,i + j)] + 1)

        return dp[0]


        