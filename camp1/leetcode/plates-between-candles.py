class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        temp  = []
        for i in range(len(s)):
            if s[i] == '|':
                temp.append(i)

        def search(num,flag):
            l = 0
            r = len(temp)-1

            if flag:
                while l <= r:
                    mid = (l + r)//2
                    if temp[mid] >= num:
                        r = mid - 1
                    else:
                        l = mid + 1
                return temp[l] if l< len(temp) else temp[l-1]

            else:
                while l  <= r:
                    mid = (l + r)//2

                    if temp[mid] <= num:
                        l = mid + 1
                    else:
                        r = mid - 1

                return temp[r] if r >= 0 else temp[r+1]


        psum = []

        for i in range(len(s)):
            if i == 0:
                if s[i] == '*':
                    psum.append(1)
                else:
                    psum.append(0)

            elif s[i] == '*':
                psum.append(psum[-1]+1)

            else:
                psum.append(psum[-1])
        
        ans = []

        for i in queries:
            if temp:
                left =  search(i[0],True)
                right = search(i[1],False)

                res = psum[right] - psum[left]
                if res < 0:
                    ans.append(0)
                else :
                    ans.append(res)
            else:
                return [0]
            
        return ans       