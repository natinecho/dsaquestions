class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        l, r = 0, len(mat[0]) - 1

        def check(mid,maxr):
            maxleft =  ( mid == 0 or mat[maxr][mid] > mat[maxr][mid - 1] )
            maxright = ( mid == len(mat[0]) - 1 or mat[maxr][mid] > mat[maxr][mid + 1] )

            return maxleft == maxright and maxright == True
        
        while l <= r:
            mid = (l + r) // 2
            
            maxr = 0
            for i in range(len(mat)):
                if mat[i][mid] > mat[maxr][mid]:
                    maxr = i
            
            if check(mid,maxr):
                return [maxr, mid]
            
            if mid > 0 and mat[maxr][mid - 1] > mat[maxr][mid]:
                r = mid - 1
            else:
                l = mid + 1 
        
        return [0, 0]
