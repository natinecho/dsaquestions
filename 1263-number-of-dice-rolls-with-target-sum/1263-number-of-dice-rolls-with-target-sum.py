class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = {}
        MOD = pow(10, 9) + 7

        def back(tar, nn):
            if (tar, nn) in dp:
                return dp[(tar, nn)]

            if nn == 0:
                return 1 if tar == target else 0

            if tar > target:
                return 0

            summ = 0

            for i in range(1, k + 1):
                summ += back(tar + i, nn - 1)
                summ %= MOD 

            dp[(tar, nn)] = summ
            return dp[(tar, nn)]

        return back(0, n)
