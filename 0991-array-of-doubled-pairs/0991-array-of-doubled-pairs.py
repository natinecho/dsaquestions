class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        count = 0
        di = {}
        arr.sort(key = lambda x:abs(x),reverse = True)

        for val in arr:
            if val * 2 in di:
                count += 1
                di[val * 2] -= 1

                if di[val * 2] == 0:
                    del di[val * 2]
            else:
                if val in di:
                    di[val] +=  1
                else:
                    di[val] = 1
        
        return count >= len(arr)//2