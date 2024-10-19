class Solution:
    def numTrees(self, n: int) -> int:
        
        # def back(arr):
        #     tt = tuple(arr)
        #     if tt not in dp:
        #         if len(arr) == 1:
        #             dp[tt] = 1
        #         else:
        #             temp = 0
        #             for i in range(len(arr)):
        #                 zz = back(arr[:i]) + back(arr[i + 1:])
        #                 temp += zz
                        
        #             dp[tt] = temp + 1

        #     return dp[tt]

        # dp = {}
        # arr = [i for i in range(1,n + 1)]

        # ans = back(arr)
        # print(dp)
        # return ans
        
        def back(val):
            if val not in dp:
                if val <= 2  :
                    dp[val] = val
                    return val
                
                temp = 0
                for i in range(val):
                    ll = 1
                    rr = 1
                    if i != 0:
                        ll = back(i) 
                        
                    if ( val - (1 + i)) != 0:
                        rr = back(val - (1 + i))

                    temp += (ll * rr)

                dp[val] = temp

            return dp[val]

            
        dp = {}

        ans = back(n)
        return ans

                

                    