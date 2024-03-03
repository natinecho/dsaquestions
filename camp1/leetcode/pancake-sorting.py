class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        sort = sorted(arr, reverse = True)
        ans = []

        r = len(arr)-1

        for i in range(len(sort)):
            idx = arr.index(sort[i])
            arr[:idx+1] = arr[:idx+1][::-1]

            ans.append(idx+1)
            ans.append(r+1)

            arr[:r+1] = arr[:r+1][::-1]
            if arr == sort[::-1]:
                break

            r-=1
        return ans
        
            


