class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        count = 0

        for i in range(1,len(timeSeries)):
            count += min(timeSeries[i] - timeSeries[i-1], duration)
        
        count += duration

        return count
        