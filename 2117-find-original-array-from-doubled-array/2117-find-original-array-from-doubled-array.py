class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort(reverse = True)
        ans = []

        di = defaultdict(int)

        for val in changed:
            if val * 2 in di:
                di[val * 2] -= 1
                ans.append(val)

                if di[val*2] == 0:
                    del di[val*2]
            
            else:
                di[val] += 1




        return ans if len(ans)*2 == len(changed) else []
        