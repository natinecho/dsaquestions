class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l  = 0 
        r = len(nums) -1 


        while l <= r:
            mid = (l + r)//2

            if mid >= 1 and nums[mid] == nums[mid -1]:
                if mid % 2 == 1:
                    l = mid + 1
                else:
                    r = mid
            elif mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                if mid % 2 == 0:
                    l = mid + 1
                else:
                    r = mid

            else:
                print(mid,nums[mid])
                return nums[mid]


        return nums[r]
        