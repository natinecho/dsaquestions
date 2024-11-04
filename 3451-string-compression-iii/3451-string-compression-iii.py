class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        i = 0
        ans = []

        while i < n:
            temp = word[i]
            count = 0

            while i < n and word[i] == temp and count < 9: 
                count += 1
                i += 1
            
            
            ans.append(str(count))
            ans.append(temp)

        return "".join(ans)

        