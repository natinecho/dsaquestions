class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp = {}

        # def back(day,status):
        #     if (day,status) in dp :
        #         return dp[(day,status)]

        #     if day >= len(prices):
        #         return 0
            
        #     if status:
        #         sell = prices[day] + back(day + 1,False)
        #         leave = back(day + 1 ,status)
        #         dp[(day,status)] = max(sell, leave)
        #     else:
        #         buy = back(day + 1 , True) - prices[day]
        #         leave = back(day + 1, status)
        #         dp[(day,status)] = max(buy, leave)
            
        #     return dp[(day,status)]
        
        # return back(0,False)


        buy = prices[0] 
        sell = profit = 0

        for i in range(len(prices)):
            if prices[i] >= sell:
                sell = prices[i]
            else:
                profit += (sell - buy)
                sell = prices[i]
                buy = prices[i]
                
        profit += (sell - buy)
        return profit



            