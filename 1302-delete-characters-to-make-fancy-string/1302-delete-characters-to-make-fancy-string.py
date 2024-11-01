class Solution:
    def makeFancyString(self, s: str) -> str:
         cc = 0
         arr = []

         for i in range(len(s)):
            # print(arr,cc)
            if arr and arr[-1] == s[i]:
                if cc != 2:
                    cc += 1
                    arr.append(s[i])
            else:
                cc = 1
                arr.append(s[i])

        
         return "".join(arr)
