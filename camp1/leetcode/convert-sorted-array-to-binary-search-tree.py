# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = None

        def divide(left , right):

            if left > right:
                return 

            if left == right:
                return TreeNode(nums[left])

            n = (right + left)//2

            l = divide(left,n-1)
            r = divide(n+1,right)

            return  TreeNode(nums[n],l,r)

        return divide(0,len(nums)-1)    