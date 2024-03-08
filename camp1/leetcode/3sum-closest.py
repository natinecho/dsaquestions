class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float("inf")
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l<r:
                summ = nums[i] + nums[l] +nums[r] 
                if summ == target:
                    return target
                elif summ > target:
                    if abs(summ - target) < abs(ans - target):
                        ans = summ
                    r -= 1
                else:
                    if abs(summ - target) < abs(ans - target):
                        ans = summ
                    l += 1
        return ans
         