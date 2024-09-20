class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:

        ks = []
        nums.sort()

        minn = nums[0]

        for i in range(len(nums)):
            if nums[i] - minn >= 2 and (nums[i] - minn) % 2 == 0:
                ks.append(nums[i] - minn)

        
        def helper(k):
            di = defaultdict(int)
            ans = []

            for val in nums[::-1]:
                if val + k in di:
                    di[val + k] -= 1
                    ans.append(val + (k//2))

                    if di[val + k] == 0:
                        del di[val + k]
                
                else:
                    di[val] += 1

            # print(di)
            return ans

        for k in ks:
            res = helper(k)
            if len(res) * 2 == len(nums):
                return res


        return []

        # print(ks)

        