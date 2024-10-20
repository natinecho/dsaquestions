class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []

        for i in range(len(nums)):
            heappush(heap,-nums[i])

        score = 0
        
        while k > 0:
            num = heappop(heap)
            score += abs(num)
            heappush(heap, - ceil(abs(num)/3))
            k -= 1

        return score
        

        
        