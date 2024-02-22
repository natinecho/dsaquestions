class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        unreach=1
        index=0
        pach=0
        while unreach<=n:
            if index<len(nums) and unreach>=nums[index]:
                unreach+=nums[index]
                index+=1
            else:
                unreach*=2
                pach+=1
        return pach

        



        