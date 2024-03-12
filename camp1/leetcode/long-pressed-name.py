class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l = 0 
        r = 0
        while l < len(name) and r < len(typed):
            cn = 0
            ct = 0
            if name[l] == typed [r]:
                while l < len(name)-1 and name[l] == name[l+1]  :
                    cn += 1
                    l += 1
                while r < len(typed)-1 and typed[r] == typed[r+1] :
                    ct += 1
                    r += 1 
            else:
                return False   
                    
            l += 1
            r += 1
            if cn > ct:
                return False

        if l < len(name) or r < len(typed):
            return False
        return True
        
