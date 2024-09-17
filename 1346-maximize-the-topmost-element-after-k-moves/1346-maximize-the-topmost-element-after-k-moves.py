class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k%2 == 1 and len(nums) == 1:
            return  -1

        nums= nums[::-1]
        maxx = max(nums)
        curr = 0

        for i in range(k):
            if i == k - 1:
                if  len(nums) >= 2 and nums[-2] > curr:
                    curr = max(curr,nums.pop())
                else:
                    nums.append(curr)       
            elif curr != maxx:
                curr = max(curr,nums.pop())
            else:
                return maxx

        return nums[-1]






        