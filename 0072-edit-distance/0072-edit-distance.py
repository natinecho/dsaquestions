class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [i for i in range(len(word1), -1, -1)]

        for i in range(len(word2) - 1,-1,-1):
            curr = [0]*(len(word1) + 1)
            curr[-1] = (len(word2) - i)
            
            for j in range(len(word1) -1, -1, -1):
                curr[j] = 0

                delete = 1 + curr[j + 1]
                insert = 1 + dp[j]
                replace = 1 + dp[j + 1]  
                leave = dp[j + 1]

                curr[j] += min(delete, insert ,replace if word2[i] != word1[j] else leave )


            
            dp = curr

        

        return dp[0]





        