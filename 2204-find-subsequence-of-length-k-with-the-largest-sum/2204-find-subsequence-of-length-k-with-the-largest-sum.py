class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        temp = defaultdict(int)

        for ni in sorted(nums,reverse= True)[:k]:
            temp[ni] += 1

        l = 0

        arr = []

        for i in range(len(nums)):
            if l < k and nums[i] in temp:
                arr.append(nums[i])
                temp[nums[i]] -= 1

                if temp[nums[i]] == 0:
                    del temp[nums[i]]
            

        return arr
