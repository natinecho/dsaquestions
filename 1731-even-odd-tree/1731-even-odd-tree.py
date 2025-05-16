# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        que = deque([root])

        level = 0


        while que:
            if level % 2 == 0:
                if que[0].val% 2 == 0:
                    return False
                for i in range(1, len(que)):
                    if que[i].val % 2 == 0 or  que[i].val <= que[i - 1].val:
                        return False
            if level % 2 == 1:
                if que[0].val% 2 == 1:
                    return False
                
                for i in range(1, len(que)):
                    if que[i].val % 2 == 1 or que[i].val >= que[i - 1].val:
                        return False

            for i in range(len(que)):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            level += 1

        
        return True


        