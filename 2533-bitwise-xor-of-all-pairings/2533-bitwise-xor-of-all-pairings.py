class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        def help(nums,n):
            val = 0
            if n % 2 != 0:
                for num in nums:
                    val ^= num

            return val

        return help(nums1,len(nums2)) ^ help(nums2,len(nums1))
