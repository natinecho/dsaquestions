class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        if (k-1)%2 == 0:
            return self.kthGrammar(n-1,k//2 + k%2)
        else:
            if self.kthGrammar(n-1,k//2 + k%2) == 1:
                return 0
            else:
                return 1
