class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []

        for i in range(len(matrix)):
            arr.extend(matrix[i])

        temp = heapify(arr)
        ans = 0
        while k > 0:
            ans = heappop(arr)
            k -= 1

        return ans