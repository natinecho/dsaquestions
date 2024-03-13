class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sc = Counter(s1)
        res = Counter()

        l = 0 

        for i in range(len(s2)):
                
            if s2[i] in res:
                res[s2[i]] += 1
            else:
                res[s2[i]] = 1
            
            if i >= len(s1):
                res[s2[l]] -= 1
                if res[s2[l]] == 0:
                    del res[s2[l]]
                l +=1
            if res == sc:
                return True
                
        return False     