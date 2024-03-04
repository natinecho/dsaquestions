class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backTrack(num,path):

            if sum(path)== target:
                ans.append(path.copy())
                return 
            if sum(path)> target:
                return 
            
            for i in range(num,len(candidates)):
                path.append(candidates[i])
                backTrack(i,path)
                path.pop()
        
        ans = []
        backTrack(0,[])

        return ans
        