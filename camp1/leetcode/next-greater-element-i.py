class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[-1]*len(nums1)
        d={}
        for i in range(len(nums2)):
            d[nums2[i]]=i
        for i in range(len(nums1)):
            temp=d[nums1[i]]
            while temp<len(nums2):
                if nums2[temp]>nums1[i]:
                    st[i]=nums2[temp]
                    break
                temp+=1
        return st      