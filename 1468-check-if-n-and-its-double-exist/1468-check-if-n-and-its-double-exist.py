class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

      
        for i in arr:
            if i in seen:
                return True
            seen.add(i / 2)
            seen.add(i  * 2)


        return False