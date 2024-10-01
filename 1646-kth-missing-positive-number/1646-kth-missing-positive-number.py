class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr) - 1

        while l <= r:
            mid = (l + r)//2

            if arr[mid] - (mid + 1) >= k:
                r = mid - 1
            else:
                l = mid + 1

        

        if r >= 0:
            return arr[r] + (k - (arr[r] - (r + 1)))

        return k


