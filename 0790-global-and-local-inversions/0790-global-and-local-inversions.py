class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        maxx1 = nums[0]
        maxx2 = -1

        for i in range(1,len(nums)):
            # print(maxx1,maxx2)
            if nums[i] >= nums[maxx1]:
                maxx2 = maxx1
                maxx1 = i
            elif nums[i] >= nums[maxx2] and maxx1 > maxx2 :
                maxx2 = i
            else:
                return False

        return True