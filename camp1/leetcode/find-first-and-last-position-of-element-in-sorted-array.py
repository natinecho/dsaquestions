class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r =len(nums)-1
        ft = -1
        ls = -1

        while l<=r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                ft = mid
                r = mid-1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        
        if ft == -1:
            return [-1,-1]

        l = ft
        r = len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                ls = mid
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1

        return [ft,ls]    