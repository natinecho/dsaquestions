class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        di = {}

        for i in range(len(nums)):
            if i in di:
                continue
            l = i
            k = 0 
        
            while l not in di:
                di[l] = 1
                temp = l
                l = l + nums[l]

                if l >=len(nums) or l < 0:
                    l = l % len(nums)

                if nums[temp] * nums[l] <0:
                    k += 1

                if l in  di and l != temp and k<1:
                    return True
            di.clear()


        return False        
            

        