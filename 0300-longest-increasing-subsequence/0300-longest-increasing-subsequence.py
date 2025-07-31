class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
            sub = []  # track smallest possible value for that subsequence length 
            for val in nums:
                i = bisect_left(sub, val)
                if i == len(sub):
                    sub.append(val)
                else:
                    sub[i] = val
            return len(sub)
        
            

        



    


        