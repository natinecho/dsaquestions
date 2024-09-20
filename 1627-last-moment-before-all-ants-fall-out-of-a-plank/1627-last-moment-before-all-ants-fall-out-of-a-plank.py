class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        
        maxx = 0

        for i in left:
            maxx = max(maxx,i)

        for i in right:
            maxx = max(maxx,n - i)

        return maxx