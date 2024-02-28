# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        ans=root
        if not root:
            root=TreeNode(val,None,None)

        def traverse(node,val):
            if node:
                if node.val>val:
                    if not node.left:
                        node.left=TreeNode(val,None,None)
                    traverse(node.left,val) 
                if node.val<val:
                    if not node.right:
                        node.right=TreeNode(val,None,None)
                    traverse(node.right,val)
        traverse(ans,val)

        return root
