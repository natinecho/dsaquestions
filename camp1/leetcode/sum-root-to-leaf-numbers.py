# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res=[]
        def traverse(node,ans):  

            if node:
                ans+=str(node.val)
                
            if not node.left and not node.right:
                res.append(ans)
                
            if node.left:
                traverse(node.left,ans)
            
            if node.right:
                traverse(node.right,ans)
        
                
        traverse(root,"")

        return sum(map(int,res))