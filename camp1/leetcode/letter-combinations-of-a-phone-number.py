class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        di = {
            "2" : ["a","b",'c'],
            "3" : ["d","e",'f'],
            "4" : ["g","h",'i'],
            "5" : ["j","k",'l'],
            "6" : ["m","n",'o'],
            "7" : ["p","q",'r','s'],
            "8" : ["t","u",'v'],
            "9" : ["w","x",'y','z'],
        }
        
        ans = []
        path = []

        def backTrack(i):
            if len(digits) == len(path):   
                ans.append("".join(path.copy()))
                return 
                
            if i >= len(digits):
                return 

            temp = di[digits[i]]

            for j in range(len(temp)):
                path.append( temp[j])
                backTrack(i+1)
                path.pop()

        if not digits:
            return []

        backTrack(0)

        return ans
