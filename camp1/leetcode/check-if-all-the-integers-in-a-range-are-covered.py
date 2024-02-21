class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        sets=set()
        for i in ranges:
            for j in range(i[0],i[1]+1):
                sets.add(j)
        print(sets)
        while left<=right:
            if left not in sets:
                return False
            left+=1
        return True

        

        