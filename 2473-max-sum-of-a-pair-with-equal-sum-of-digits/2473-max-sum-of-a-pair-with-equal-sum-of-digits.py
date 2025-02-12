class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        store = {}

        for val in nums:
            temp = sum(map(int,list(str(val))))
            if temp in store:
                ans = max(ans,store[temp] + val)
                store[temp] = max(store[temp],val)
            else:
                store[temp] = val



        return ans
        