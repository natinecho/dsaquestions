class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pcount = Counter(p)
        scount = Counter()
        res = []
        l = 0
        for i in range(len(s)):
    
            if s[i] in scount:
                scount[s[i]] += 1
            else:
                scount[s[i]] = 1
            
            if i>= len(p):
                scount[s[l]] -= 1
                if scount[s[l]] == 0:
                    del scount[s[l]]
                l +=1
            if scount == pcount:
                res.append(l)
                
        return res

            
