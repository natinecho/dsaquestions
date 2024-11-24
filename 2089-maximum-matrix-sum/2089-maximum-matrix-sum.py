class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        arr = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                arr.append(matrix[i][j])
        
        arr.sort()

        ind  = bisect_left(arr,0)
        
        
        summ = sum(abs(i) for i in arr) 
        minn = min(abs(i) for i in arr) 

        return summ if ind % 2 == 0 else summ - (2 * minn)

        

        