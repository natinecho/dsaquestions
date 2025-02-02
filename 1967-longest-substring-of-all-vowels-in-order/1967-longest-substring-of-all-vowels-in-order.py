class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = "aeiou"
        maxx = 0

        l = 0
        i = 0
        last = "a"
        cc = 0

        while i < len(word):
            if word[i] > last:
                last = word[i]
                cc += 1
            elif word[i] == last == "a" and cc == 0:
                cc += 1
    
            elif word[i] < last:
                if cc == 5:
                    maxx = max(maxx, i - l)

                l = i
                cc = 0
                last = "a"

                continue
            i += 1
                

        return max(maxx,i - l) if cc == 5 else maxx


   
        