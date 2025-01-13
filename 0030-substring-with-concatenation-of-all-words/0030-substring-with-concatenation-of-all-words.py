class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        count = Counter(words)
        n,m,k = len(s),len(words),len(words[0])

        ans = []
        for i in range(k):
            l = r = i
            cc = 0
            temp = Counter()

            while r + k <= n:
                word = s[r:r + k]

                r += k

                if word not in count:
                    l = r 
                    temp.clear()
                    cc = 0
                else:
                    temp[word] += 1
                    cc += 1
                    while temp[word] > count[word]:
                        ww = s[l:l + k]
                        temp[ww] -= 1
                        cc -= 1
                        l += k
                    
                    if cc == m:
                        ans.append(l)

        return ans