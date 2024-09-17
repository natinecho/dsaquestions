class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        seen = set()
        ugly = sorted(primes)
        heap = [1]

        while n > 1:
            # print(heap)
            node = heappop(heap)
            n -= 1
            for i in ugly:
                if node * i not in seen:
                    heappush(heap,node * i)
                    seen.add(node * i)
                    # n -= 1
        return heap[0]