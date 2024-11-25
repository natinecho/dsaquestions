class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        i, j = 0, 0
        star = -1
        back_pos = -1

        while i < n:
            if j < m and (s[i] == p[j] or p[j] == "?"):
                i += 1
                j += 1

            elif j < m and p[j] == "*":
                star = j  
                back_pos = i 
                j += 1

            elif star != -1:
                i = back_pos + 1  
                j = star + 1  
                back_pos += 1

            else:
                return False
                

        for k in range(j, m):
            if p[k] != "*":
                return False

        return True
