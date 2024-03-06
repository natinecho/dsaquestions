class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        r = sum(weights)
        ans = 0

        while l<=r:
            val = (l+r)//2
           
            tot = 0
            count = 1
            for i in range(len(weights)):
                if tot + weights[i]<=val:
                    tot += weights[i]
                else:
                    count += 1
                    tot = weights[i]
            if count <= days:
                ans = val
                r = val -1
            else:
                l = val + 1

        return ans


            
        