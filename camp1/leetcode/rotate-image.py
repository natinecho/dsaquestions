class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in  range(len(matrix)):
            
            for j in range(len(matrix)-1,i-1,-1):

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            first=0
            last=len(matrix)-1

            while last>first:
                matrix[i][first], matrix[i][last] = matrix[i][last], matrix[i][first]
                last-=1
                first+=1
        
        return matrix
            


        