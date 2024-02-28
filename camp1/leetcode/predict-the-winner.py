class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:     
        def game(l,r):
            left_res=0
            right_res=0
            if l==r:
                return nums[l]
            left_res=nums[l]- game(l+1,r)
            right_res=nums[r]-game(l,r-1)
            return max(left_res,right_res)
        
        return game(0,len(nums)-1)>=0
