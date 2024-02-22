class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        de=deque()
        for i in tickets:
            de.append(i)
        flag=k
        time=0
        while de and  de[flag]!=0:
            a=de.popleft()
            if a!=0:
                time+=1
                de.append(a-1)
            flag-=1
           
            if flag==-1:
                flag=len(de)-1
           
            
        return time



        