# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        temp = []
        def trav(node):
            if node:
                trav(node.left)
                temp.append(node.val)
                trav(node.right)
        trav(root)
        
        def div(l,r):
            if r>l:
                n = (l+r)//2
                left = div(l,n)
                right = div(n+1,r)
                return TreeNode(temp[n],left,right)
                
        return div(0,len(temp))
        