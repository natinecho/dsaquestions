class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        temp = {}

        for i in range(len(mat)):
            for j in range( len(mat[0])):
                if i+j in temp:
                    temp[i+j].append(mat[i][j])
                else:
                    temp[i+j]= [mat[i][j]]
        ans = []
        print(temp)
        
        for i,k in temp.items():
            if i%2==0:
                ans.extend(k[::-1])
            else:
                ans.extend(k)

        return ans



