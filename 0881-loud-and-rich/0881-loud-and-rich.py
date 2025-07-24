class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indgree = defaultdict(int)

        for src,des in richer:
            graph[src].append(des)
            indgree[des] += 1

        que = deque()
        ans = [ i for i in range(len(quiet))]

        for i in range(len(quiet)):
            if indgree[i] == 0:
                que.append(i)

        while que:
            node = que.pop()
            for ni in graph[node]:
                indgree[ni] -= 1

                if quiet[ans[ni]] > quiet[ans[node]]:
                    ans[ni] = ans[node]
                    
                if indgree[ni] == 0: 
                    que.append(ni)
        
        return ans




        