class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = []

        for i in strs:
            res.append(list(i))
        
        count=0

        for i in range(len(res[0])):
            for j in range(len(res)-1):
                if res[j][i]>res[j+1][i]:
                    count+=1
                    break
            

                

        return count
