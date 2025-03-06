class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        dup = -1
        miss = -1


        for row in grid:
            for val in row:
                if val in seen:
                    dup = val
                
                seen.add(val)

        for i in range(1, len(grid) * len(grid) + 1):
            if i not in seen:
                miss = i 

        
        return [dup,miss]

        