# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode], minn=float('inf'), maxx=float('-inf')) -> int:
        ans = 0
        
        def help(node):
            nonlocal ans
            if node:
                left_min = help(node.left) if node.left else [node.val, node.val]

                right_min= help(node.right) if node.right else [node.val, node.val]
                
                l = min(node.val, left_min[0], right_min[0])
                r = max(node.val, left_min[1], right_min[1])

                ans = max(ans, max(abs(l - node.val), abs(r - node.val)))

                return [l,r]

        help(root)
        
        return ans

                
            


