class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []

        if a > 0: heappush(heap,(-a,"a"))
        if b > 0: heappush(heap,(-b,"b"))
        if c > 0: heappush(heap,(-c,"c"))
        ans = []

        while heap:
            num,char = heappop(heap)

            if len(ans) >= 2 and ans[-1] == ans[-2] == char:
                if heap:
                    nn,ch = heappop(heap)
                    ans.append(ch)
                    if nn + 1 < 0:
                        heappush(heap,(nn + 1, ch))
                else:
                    break

            ans.append(char)
            if num + 1 < 0:
                heappush(heap,(num + 1,char))


        
        return "".join(ans)
