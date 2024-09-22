class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False] *(n + 1)

        def divisors(num):
            lim = int(sqrt(num))
            arr = []

            for i in range(1,lim + 1):
                if i != num and  num % i == 0:
                    arr.append(i)
                    if i != 1:
                        arr.append(num // i)

            return arr

        for num in range(1,n + 1):
            arr = divisors(num)
            temp = False

            for ni in arr:
                if not dp[num - ni]:
                    dp[num] = True
                    break




        return dp[n]