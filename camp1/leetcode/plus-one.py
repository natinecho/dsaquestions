class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        revd=digits[::-1]
        carry=0
        if revd[0]<9:
            revd[0]+=1
        else:
            for i in range(len(revd)):
                if revd[i]<9:
                    revd[i]+=carry
                    carry=0
                    break
                else:
                    carry=1
                    revd[i]=0
            if carry==1:
                revd.append(1)
        return revd[::-1]
            
        