class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        st=[]
        d={}
        res=[-1]*n
        f=0
        temp= nums.copy()
        for i in range(n):
            nums.append(nums[i])

        for i in range(len(nums)):
            while st and nums[st[-1]]<nums[i]:
                a=st.pop()
                d[a]=nums[i]
            st.append(i)
        
        for i in range(len(temp)):
            if i in d:
                res[i]=d[i]

        return res

        