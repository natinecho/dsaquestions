class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cc = Counter(nums)
        ans = []

        maxx = len(nums)/3

        for k,v in cc.items():
            if v > maxx:
                ans.append(k)

        return ans

        