class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxx = 0
        diag = 0

        for di in dimensions:
            temp = sqrt((di[0]**2) + (di[1]**2))


            if temp == diag:
                diag = max(diag,temp)
                maxx = max(maxx,di[0] * di[1])
            elif temp > diag :
                diag = max(diag,temp)
                maxx = di[0] * di[1]

        
        return maxx


        