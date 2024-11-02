class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        arr = sentence.split()

        temp = []

        for ss in arr:
            if temp and temp[-1][1] != ss[0]:
                return False
            else:
                temp.append([ss[0],ss[-1]])

        return True if temp[-1][1] == temp[0][0] else False


        