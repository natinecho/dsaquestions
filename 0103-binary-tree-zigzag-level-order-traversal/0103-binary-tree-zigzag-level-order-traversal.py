# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        ans = []
        que = deque([root])
        flag = True

        while que:
            level_size = len(que)
            level = deque()

            for _ in range(level_size):
                node = que.popleft()

                if flag:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                    
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            ans.append(list(level))
            flag = not flag
        
        return ans
