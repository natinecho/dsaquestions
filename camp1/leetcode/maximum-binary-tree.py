# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def div(l,r):
            if r>l:
                num = max(nums[l:r])
                temp = nums.index(num)
                left = div(l,temp)
                right = div(temp+1,r)
                return TreeNode(num,left,right)
        return div(0,len(nums))
        