class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        ans = 0
        c = Counter(nums)
        s = sorted(list(set(nums)),reverse = True)

        for i in range(len(s)-1):
            ans+=c[s[i]]
            c[s[i+1]] += c[s[i]]

        
        return ans

        