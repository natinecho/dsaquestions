class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def isVawel(i):
            return i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'

        c = 0 
        l = 0
        maxx = 0       
        for i in range(len(s)):
            if isVawel( s[i] ):
                c += 1
            if i >= k:
                if isVawel( s[l] ):
                    c -= 1
                l += 1
            maxx = max(maxx,c)

        return maxx