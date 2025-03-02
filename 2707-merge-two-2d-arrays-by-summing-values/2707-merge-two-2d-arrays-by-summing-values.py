class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = {}

        for idx,val in nums1:
            ans[idx] = ans.get(idx,0) + val
        
        for idx,val in nums2:
            ans[idx] = ans.get(idx,0) + val

        return sorted([key,ans[key]] for key in ans)

        