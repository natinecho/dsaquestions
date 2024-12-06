class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        seen = set(banned)

        cc = 0
        pre = 0


        for i in range(1,n + 1):
            if i not in seen and pre + i <= maxSum:
                cc += 1
                pre += i

        return cc
