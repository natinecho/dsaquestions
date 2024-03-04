class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        temp = []
        def backTrack(i):
            if len(temp) == k:
                if sum(temp) == n:
                    res.append(temp.copy())
            
            for j in range(i+1, 10):
                temp.append(j)
                backTrack(j)
                temp.pop()

        backTrack(0)
       
        return res

        