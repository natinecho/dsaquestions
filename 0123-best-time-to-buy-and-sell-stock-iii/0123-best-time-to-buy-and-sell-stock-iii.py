class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dp(day,status,transaction):

            if (day,status,transaction) in memo:
                return memo[(day,status,transaction) ]

            if day >= len(prices):
                return 0

            leave = dp(day + 1,status,transaction)
            
            if transaction  < 2:
                if status:
                    sell = dp(day + 1,False,transaction) +  prices[day]
                    memo[(day,status,transaction) ] =  max(sell,leave) 

                else:
                    buy = dp(day + 1,True,transaction + 1) - prices[day]
                    memo[(day,status,transaction) ] =  max(buy,leave) 

            elif transaction  == 2  and status:
                sell = dp(day + 1,False,transaction) +  prices[day]
                memo[(day,status,transaction) ] =  max(sell,leave) 
            
            else:
                memo[(day,status,transaction) ] = 0


            return memo[(day,status,transaction) ]

        return dp(0, False, 0)





   
