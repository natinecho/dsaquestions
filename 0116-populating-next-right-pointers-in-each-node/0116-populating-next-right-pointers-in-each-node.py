"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        if not root:
            return None

        # root.next = None
        que = deque([root])

        while que:
            # temp = []
            n = len(que)
            for i in range(n):
                node = que.popleft()
                if i == n - 1:
                    node.next = None
                else:
                    node.next = que[0]


                if node.left:
                    que.append(node.left)
                
                if node.right:
                    que.append(node.right)

        return root


        
        
        