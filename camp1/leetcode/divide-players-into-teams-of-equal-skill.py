class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        tot= max(skill)+min(skill)
        r=len(skill)-1
        l=0
        res=0

        while l<r:
            temp=skill[l]+skill[r]
            if temp!=tot:
                return -1
            else:
                res+=(skill[l]*skill[r])
                l+=1
                r-=1
        return res
        