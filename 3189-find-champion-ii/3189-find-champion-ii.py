class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        indgree = defaultdict(int)

        for stronger, week in edges:
            graph[stronger].append(week)
            indgree[week] += 1
        
        ans = []
        for i in range(n):
            if indgree[i] == 0:
                ans.append(i)
        
        return ans[0] if len(ans) == 1 else -1
        