class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        sets = set()
        ans = 0
        summ = 0
        l = 0

        for i in range(len(nums)):
            while nums[i] in sets and l < i:
                summ -= nums[l]
                sets.remove(nums[l])
                l += 1

            sets.add(nums[i])
            summ += nums[i]

            if i - l + 1 == k:
                ans = max(ans,summ)
                sets.remove(nums[l])
                summ -= nums[l]
                l += 1
                
        
        if i - l + 1 == k:
            ans = max(ans,summ)


        return ans
            

        