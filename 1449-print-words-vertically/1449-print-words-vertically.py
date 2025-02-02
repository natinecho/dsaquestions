class Solution:
    def printVertically(self, s: str) -> List[str]:
        arr = s.split()
        ans = []

        lenn = max(len(word) for word in arr)

        for i in range(lenn):
            temp = ""
            for j in range(len(arr)):
                if i >= len(arr[j]):
                    temp += " "
                else:
                    temp += arr[j][i]

            ans.append(temp.rstrip())

        
                
                
        return ans

        