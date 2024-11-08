class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        def help(nums,n):
            arr = [0]*32

            for num in nums:
                for i in range(32):
                    arr[i] += 1 if (num & (1 << i)) else 0
            
            # print(arr)

            for i in range(32):
                arr[i] = (arr[i] * n)%2

            ans = 0
            
            for i in range(32):
                ans |= (arr[i] << i)

            return ans

            
        return help(nums1, len(nums2)) ^ help(nums2, len(nums1))