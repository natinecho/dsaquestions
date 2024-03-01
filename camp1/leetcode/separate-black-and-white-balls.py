class Solution:
    def minimumSteps(self, s: str) -> int:
        arr=list(s)
        n=len(s)
        l=n-2
        r=n-1
        count=0
        if n==1:
            return 0

        while r>=0 and l>=0:
            if arr[l]=='0' and arr[r]!=arr[l]:
                r=l
            if arr[l]=='1' and arr[r]=='0':
                arr[l],arr[r]=arr[r],arr[l]
                count+=(r-l)
                r-=1

            l-=1

        return count
            
        