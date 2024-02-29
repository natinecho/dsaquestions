# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode], minn=100000,maxx=0) -> int:
        if not root:
            return maxx-minn
            
        minn=min(minn,root.val)
        maxx=max(maxx,root.val)

        return max(self.maxAncestorDiff(root.left,minn,maxx) , self.maxAncestorDiff(root.right,minn,maxx))       