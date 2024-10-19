class Solution:
    def numTrees(self, n: int) -> int:     
        # def back(val):
        #     if val not in dp:
        #         if val <= 2  :
        #             dp[val] = val
        #             return val
                
        #         temp = 0
        #         for i in range(val):
        #             ll = 1
        #             rr = 1
        #             if i != 0:
        #                 ll = back(i) 
                        
        #             if ( val - (1 + i)) != 0:
        #                 rr = back(val - (1 + i))

        #             temp += (ll * rr)

        #         dp[val] = temp

        #     return dp[val]

            
        # dp = {}

        # ans = back(n)
        # return ans

        dp = [1]*(n + 1)

        for val in range(2,n + 1):

            temp = 0
            for i in range(val):
                ll = 1
                rr = 1
                if i != 0:
                    ll = dp[i]
                    
                if ( val - (1 + i)) != 0:
                    rr = dp[val - (1 + i)]

                temp += (ll * rr)

            dp[val] = temp


        return dp[n]


                    