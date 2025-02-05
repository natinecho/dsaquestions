class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        temp1 = []
        temp2 = []

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                temp1.append(s1[i])
                temp2.append(s2[i])

        temp1.sort() 
        temp2.sort() 

        return temp1 == temp2 and (len(temp1) == 0 or len(temp2) == 2)
                
                

