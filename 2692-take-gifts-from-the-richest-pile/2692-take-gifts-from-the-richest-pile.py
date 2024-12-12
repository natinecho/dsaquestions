class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []

        for i in range(len(gifts)):
            heappush(heap,-gifts[i])

        while k > 0:
            node = -heappop(heap)
            heappush(heap,-int(sqrt(node)))

            k -= 1

        return -sum(heap)
