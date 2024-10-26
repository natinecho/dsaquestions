# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:


        def height(node):
            if not node:
                return 0

            ll = height(node.left) + 1
            rr = height(node.right) + 1

            memo[node.val] = [ll,rr]
            return max(ll ,rr)

        memo = {}
        ans = {}

        height(root)


        def calc():
            st = [(root,0,0)]

            while st:
                node,maxx,h = st.pop()
                ans[node.val] = maxx - 1

                if node.left:
                    st.append((node.left,max(maxx,h + memo[node.val][1]), h + 1))

                if node.right:
                    st.append((node.right,max(maxx,h + memo[node.val][0]),h + 1))

        calc()
        
        res = []

        for qq in queries:
            res.append(ans[qq])


        return res
        