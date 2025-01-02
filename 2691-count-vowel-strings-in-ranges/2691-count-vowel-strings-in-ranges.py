class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        psum = [0]
        vowel = "aeiou"
        for i in words:
            if i[-1] in vowel and i[0]  in vowel:
                psum.append(psum[-1] + 1)
            else:
                psum.append(psum[-1])
        ans = []
        for i,j in queries:
            ans.append(psum[j + 1] - psum[i])
        
        return ans