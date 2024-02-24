class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
            # res=[]
            # l,r=0,0
            # while r <len(nums):
            #     if nums[l]!=nums[r]:
            #         res.append(nums[l])
            #         l=r
            #     r+=1
            # if l==len(nums)-1:
            #     res.append(nums[l])
            res=set(nums)
            nums.clear()
           
            for i in res:
                nums.append(i)
            nums.sort()
            return len(nums)



