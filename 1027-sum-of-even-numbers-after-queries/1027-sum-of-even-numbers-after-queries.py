class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summ = sum(nums[i] for i in range(len(nums)) if nums[i] % 2 == 0)
        ans = []

        for val,ind in queries:
            if nums[ind] % 2 == 0:
                if (nums[ind] + val) % 2 == 0:
                    summ += val
                else:
                    summ -= nums[ind]

            elif (nums[ind] + val) % 2 == 0:
                summ += (nums[ind] + val) 

            nums[ind] += val
            ans.append(summ)

        return ans   