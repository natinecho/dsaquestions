class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        arr = []

        for i in range(len(nums)):
            arr.append((nums[i],i))
            # print(nums[i].bit_count(),nums[i])

        arr.sort()

        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if arr[j][0].bit_count() != arr[i][0].bit_count() and arr[j][1] < arr[i][1]:
                    return False

        return True

        