class Solution:
    def countVowels(self, word: str) -> int:
        ans = 0
        vowel =  "aeiou"
        n = len(word)

        for i in range(n):
            if word[i] in vowel:
                ans += (i + 1)*(n - i)

        return ans

        