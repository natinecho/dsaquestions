class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l=0
        r=len(people)-1
        people.sort()

        count=0
        while l<=r:
            res=people[l]+people[r]
            if res>limit:
                r-=1
            else:
                l+=1
                r-=1
            count+=1
        return count
        