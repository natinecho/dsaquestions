class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        new = colors * 2
        l = 0
        ans = 0 
         
        for i in range(1,len(colors) + k - 1):
            if new[i] == new[i - 1]:
                l = i

            if i - l + 1 >= k:
                ans += 1
                l += 1
        


        return ans
            