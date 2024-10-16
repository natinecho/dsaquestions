class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        
        heap = []

        for k,v in count.items():
            heappush(heap,(-v,k))

        ans = []

        while heap:
            num,char = heappop(heap)

            if len(ans) >= 1 and ans[-1] == char:
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


        
        return "".join(ans) if len(ans) == len(s) else ""


        
