class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1
        cz = 0

        for i in range(len(nums)):
            if nums[i]!= 0:
                pro *= nums[i]
            if nums[i] == 0:
                cz += 1
        res = []
        for i in range(len(nums)):
            if cz >= 2:
                res.append(0)
            elif cz == 1 and nums[i] == 0:
                res.append(pro)
            elif cz == 1:
                res.append(0)
            else:
                res.append(pro//nums[i])
                
        return res

                

        