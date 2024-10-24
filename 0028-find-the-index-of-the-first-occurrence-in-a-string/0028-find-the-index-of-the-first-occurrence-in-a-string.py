class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        poww = [1]
        MOD = 10 ** 9 + 7
        n = len(haystack)
        m = len(needle)

        if m > n:
            return -1


        for i in range(m):
            poww.append((poww[-1] * 27) % MOD )
        
        summ = 0 

        for  i in range(m):
            summ = ((summ *27) +  (ord(needle[i]) - 96)) % MOD

        temp = 0
        for  i in range(m):
            temp = ((temp *27) +  (ord(haystack[i]) - 96)) % MOD

        if temp == summ:
            if haystack[:m] == needle:
                return 0

        l = 0

        for i in range(m,n):
            temp -= ((ord(haystack[l]) - 96)* (poww[m - 1]))% MOD
            temp = ((temp *27) +  (ord(haystack[i]) - 96)) % MOD
            l += 1
            
            if temp == summ:
                if haystack[l:i + 1] == needle:
                    return l

        return -1
