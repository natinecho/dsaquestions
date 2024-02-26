class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]

        prev=self.getRow(rowIndex-1)
        res=[]
        res.append(1)

        for i in range(len(prev)-1):
            temp=prev[i]+prev[i+1]
            res.append(temp)
        res.append(1)

        return res

        
        