class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor_ = []
        temp = 0
        val = (1<<maximumBit) - 1
        for num in nums:
            temp ^= num
            xor_.append(temp)
        
        ans = []
        for i in xor_:
            ans.append(i ^ val)
        
        return ans[::-1]
            

        