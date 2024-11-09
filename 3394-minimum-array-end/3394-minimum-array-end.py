class Solution:
    def minEnd(self, n: int, x: int) -> int:
        ans = x
        j = 0
        for i in range(64):
            if x & (1<<i) == 0:
                if (n - 1) &(1 << j):
                    ans |= 1 << i
                j += 1

        return ans


