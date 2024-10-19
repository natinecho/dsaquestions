# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        ans   = []

        def back(l , r):

            if l > r:
                return [None]

            trees = []

            for i in range(l, r + 1):
                left = back(l,i - 1)
                right = back(i + 1, r)

                for ll in left:
                    for rr in right:
                        node = TreeNode(i)
                        node.left = ll
                        node.right = rr
                        trees.append(node)

            return trees

        
        return back(1,n)
            


        