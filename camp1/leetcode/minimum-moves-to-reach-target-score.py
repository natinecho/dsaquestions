class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        move=0
        while target>1:
            if maxDoubles==0:
                move+=(target-1)
                break
            if target%2==0 and maxDoubles>0:
                target-=(target//2)
                maxDoubles-=1
            else:
                target-=1 
            move+=1
        return move
            
            


        