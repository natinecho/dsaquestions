class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        ans = []

        for i in range(len(max(arr, key = lambda x: len(x)))):
            temp = ""
            last = 0
            for j in range(len(arr)):
                if i >= len(arr[j]):
                    temp += " "
                else:
                    temp += arr[j][i]
                    last = j

            ans.append(temp[:last + 1])

        
                
                
        return ans

        