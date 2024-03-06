class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = len(matrix[0])

        l = 0
        r = len(matrix)-1

        def find(idx):
            l = 0
            r = len(matrix[0])-1
            while l<=r:
                m = (l+r)//2
                if  matrix[idx][m]== target:
                    return True
                elif matrix[idx][m]>= target:
                    r = m -1
                else:
                    l = m + 1
            return False


        while l<= r:
            m = (l+r)//2

            if matrix[m][0]<= target and target <= matrix[m][col-1]:
                return find(m)
            elif  matrix[m][0] > target:
                r = m -1
            else:
                l = m+1

        return False



