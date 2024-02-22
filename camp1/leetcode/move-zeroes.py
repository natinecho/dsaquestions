class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # res=[]
        # for i in range(len(nums)):
        #     if len(nums) and nums[i]==0:
        #         res.append(nums[i])
        #         nums.remove(0)
        # print(nums,res)
        # nums.extend(res)
        i=0
        count=0
        while i<len(nums):
            if nums[i]==0:
                count+=1
                nums.remove(0)
                i-=1
            i+=1
        for i in range(count):
            nums.append(0)

        