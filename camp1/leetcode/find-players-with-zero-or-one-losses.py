class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win,los=defaultdict(int),defaultdict(int)
        for i in matches:
            win[i[0]]+=1
            los[i[1]]+=1
        los0=[]
        los1=[]
        for i in win:
            if i not in los: 
                los0.append(i)

        for i,k in los.items():
            if k==1: 
                los1.append(i)

        return [sorted(los0),sorted(los1)]