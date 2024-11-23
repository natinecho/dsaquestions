# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        temp = root
        if not root:
            return False

        def dfs(node,tar):
            if node.left:
               if dfs(node.left,tar + node.val):
                    return True
                
            if node.right:
                if dfs(node.right,tar + node.val):
                    return True
    
            if not node.right and not node.left:
                if tar + node.val == targetSum:
                    return True

            return False
        
        return dfs(temp, 0)