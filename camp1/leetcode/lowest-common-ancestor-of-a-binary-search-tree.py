# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find(node,key1,key2):
            if node:
                if node.val>key1 and  node.val>key2:
                    return  find(node.left,key1,key2)
                if node.val<key1 and node.val<key2:
                    return find(node.right,key1,key2)
                if node.val==key1 or node.val==key2:
                    return node
                if (node.val>key1 and node.val<key2)or (node.val<key1 and node.val>key2):
                    return node
                
            else:
                return None

        return find(root,p.val,q.val)
                

        