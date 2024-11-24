class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minn = float("inf")
        summ = 0
        count = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val = abs(matrix[i][j])
                minn = min(val,minn)
                summ += val

                if matrix[i][j] < 0:
                    count += 1
        
    
        return summ if count % 2 == 0 else summ - (2 * minn)

        

        