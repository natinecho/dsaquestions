class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans=0
        temp=0

        for i in range(len(mat)):
            for j in range(len(mat)):
                if i+j == len(mat)-1:
                    ans+=mat[i][j]
                if i-j == 0:
                    temp+= mat[i][j]

        if len(mat)%2==0:
            ans+=temp
        else:
            idx=len(mat)//2

            ans = ans + temp-mat[idx][idx]
    
        return  ans         

        