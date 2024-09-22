class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = {}

        def divisors(num):
            lim = int(sqrt(num))
            arr = []

            for i in range(1,lim + 1):
                if i != num and  num % i == 0:
                    arr.append(i)
                    if i != 1:
                        arr.append(num // i)

            return arr

        def back(num,turn):
            if num not in dp:
                arr = divisors(num)
                if turn == 1 and not arr:
                    dp[num] = False
                    return dp[num]
                
                if turn == 0 and not arr:
                    dp[num] = True
                    return dp[num]


                temp = False

                for ni in arr:
                    temp = temp or back(num - ni,1 - turn)
                
                dp[num] = temp

            return dp[num]

        back(n,1)
        return dp[n]