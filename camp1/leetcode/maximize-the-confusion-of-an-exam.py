class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        maxx = 0
        di = {'T':0,'F':0}
        l = 0

        for i in range(len(s)):
            di[s[i]] += 1
            while min(di.values()) > k:
                di[s[l]] -= 1
                l += 1
            maxx = max(maxx,i - l)
        return maxx + 1


