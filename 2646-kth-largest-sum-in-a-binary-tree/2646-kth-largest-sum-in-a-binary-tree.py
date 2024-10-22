# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

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
            

        
        arr.sort(reverse = True)

        return arr[k - 1] if k <= len(arr) else -1


