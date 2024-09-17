class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = set()
        ugly = [2,3,5]
        heap = [1]

        while n > 1:
            node = heappop(heap)
            n -= 1
            for i in ugly:
                if node * i not in seen:
                    heappush(heap,node * i)
                    seen.add(node * i)
                    # n -= 1
        return heap[0]

        