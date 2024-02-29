class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        l=r=0
        arr=[]
        last={}
        for i in range(len(s)):
            last[s[i]]=i
        r=l=0
        for i in range(len(s)):
            if i>r:
                arr.append((r-l)+1)
                l=r=i    
            if i==len(s)-1:
                 arr.append((i-l)+1)

            r=max(r,last[s[i]])
        
        return arr


        
          