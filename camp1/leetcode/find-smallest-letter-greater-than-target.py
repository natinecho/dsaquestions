class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = -1
        r = len(letters)

        while l+1< r:
            mid = (l+r)//2

            if letters[mid] <= target:
                l = mid
            else:
                r = mid
        return letters[r] if r<len(letters) else letters[0]



        # by using bisect library

        # if bisect_right(letters,target) < len(letters):
        #     return letters[bisect_right(letters,target)]
        # return letters[0]

        # using normal iteration

        # for i in range(len(letters)):
        #     if letters[i]>target:
        #         return letters[i]
        # return letters[0]

