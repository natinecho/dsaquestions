class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp=nums.copy()
        nums.clear()
        for i in temp:
            if i!=val:
                nums.append(i)
        return len(nums)

        