class Solution:
    def coloredCells(self, n: int) -> int:
        ans = 0

        while n > 1:
            ans += ((n-1)*4)
            n -= 1
        
        return ans + 1
        