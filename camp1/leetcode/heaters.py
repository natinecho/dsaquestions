class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = 0
        minn = 0
        maxx = max(max(houses),max(heaters))
    
        while  minn <= maxx:
            he = 0
            ho = 0
            mid = (minn + maxx)//2
            while ho < len(houses) and he < len(heaters):
                if abs(houses[ho]-heaters[he])> mid:
                    he +=1
                else:
                    ho +=1

            if  ho == len(houses) and he < len(heaters):
                ans = mid
                maxx = mid -1
            else:
                minn = mid + 1

        return ans