class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j,tot=0,0,0
        m=len(g)
        n=len(s)

        while n>i and m>j:
            if s[i]>=g[j]:
                tot+=1
                i+=1
                j+=1
            else:
                i+=1
        return tot
        