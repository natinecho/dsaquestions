class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def check(arr):
            for r in range(1,len(arr)):
                if arr[r] < arr[r - 1]:
                    return False

            return True

        for i in range(len(nums)):
            if check(nums[:i] + nums[i + 1:]):
                return True

        return False


