class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        res = []

        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        temp = max(d, key=lambda x: d[x]%2==1)
        for i in d:
            if i==temp:
                res.append(d[i])
            else:
                num = (d[i] // 2) * 2
                res.append(num)
             

        return sum(res)

        