class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        extended = code * 2
        result = [0] * n
        abs_k = abs(k)
        
        if k > 0:
            current_sum = sum(extended[1:1 + k]) 
            for i in range(n):
                result[i] = current_sum
                current_sum += extended[i + k + 1] - extended[i + 1]
        else:
            current_sum = sum(extended[n - abs_k:n])  
            for i in range(n):
                result[i] = current_sum
                current_sum += extended[n + i] - extended[n + i - abs_k]
        
        return result