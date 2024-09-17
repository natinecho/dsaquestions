class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        dp = [float("-inf")]*len(nums)

        dp[-1] = 0

        for i in range(len(nums) -2,-1,-1):
            for j in range(i + 1,len(nums)):

                if abs(nums[i] - nums[j]) <= target:

                    dp[i] = max(dp[i],dp[j] + 1)

        # print(dp)
        return  dp[0] if dp[0] != float("-inf") else -1 

                
        # dp = {}

        # def back(ind):
        #     if ind in dp:
        #         return dp[ind]

        #     if ind == len(nums) - 1:
        #         dp[ind] = 0
        #         return 0

        #     ans = float("-inf")

        #     for i in range(ind + 1,len(nums)):
        #         if abs(nums[ind] - nums[i]) <= target:
        #             ans = max(ans,back(i) + 1)
            
        #     dp[ind] = ans

        #     return dp[ind]

        # back(0)
        