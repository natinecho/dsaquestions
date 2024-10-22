# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        arr = []    

        que = deque([root])

        while que:
            summ = 0
            for i in range(len(que)):
                node = que.popleft()
                summ += node.val

                if node.left:
                    que.append(node.left)

                if node.right:
                    que.append(node.right)
            
            arr.append(summ)
            

        

        return arr.index(max(arr)) + 1