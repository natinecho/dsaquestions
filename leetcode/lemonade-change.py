class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d=defaultdict(int)     
        for i in bills:
            if i==5:
                d[i]+=1
            elif i==10 and d[5]>=1:
                d[5]-=1
                d[i]+=1
            elif i==20:
                if d[10]>=1 and d[5]>=1:
                    d[5]-=1
                    d[10]-=1
                elif d[5]>=3:
                    d[5]-=3
                else:
                    return False
            else:
                return False
            
        return True
        

        