class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []

        def back(arr,ind,seen):
            if ind == len(pattern):
                ans.append(arr[::])
                return 
            
        
            for i in range(1,10):
                if pattern[ind] == "I" and arr and arr[-1] < i and i not in seen:
                    arr.append(i)
                    seen.add(i)
                    back(arr,ind + 1,seen)
                    seen.discard(i)
                    arr.pop()
                elif pattern[ind] == "D" and arr and arr[-1] > i and i not in seen:
                    arr.append(i)
                    seen.add(i)
                    back(arr,ind + 1,seen)
                    seen.discard(i)
                    arr.pop()
                elif not arr:
                    arr.append(i)
                    seen.add(i)
                    back(arr,ind,seen)
                    seen.discard(i)
                    arr.pop()

            return 



        back([],0,set())

        ans.sort()

        my_Ans = ""

        for i in ans[0]:
            my_Ans += str(i)

        return my_Ans

                
