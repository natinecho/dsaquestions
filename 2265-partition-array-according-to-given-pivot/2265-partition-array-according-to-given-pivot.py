class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater = []
        smaller = []
        equal = []

        for i in range(len(nums)):
            if nums[i] > pivot:
                greater.append(nums[i])
            if nums[i] < pivot:
                smaller.append(nums[i])
            if nums[i] == pivot:
                equal.append(nums[i])
        
        return smaller + equal + greater
        