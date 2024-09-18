class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        que = deque([(x,0)])
    

        seen = set([x])

        while que:
            # print(que)
            num,count = que.popleft()

            if num == y:
                return count
            
            if num % 5 == 0 and num//5 not in seen:
                que.append((num//5,count + 1))
                seen.add(num//5)

            if num % 11 == 0 and num//11 not in seen:
                que.append((num//11,count + 1))
                seen.add(num//11)
            
            if num + 1 not in seen:
                que.append((num + 1,count + 1))
                seen.add(num + 1)

            if num - 1 not in seen:
                que.append((num - 1,count + 1))
                seen.add(num - 1)

        return -1



