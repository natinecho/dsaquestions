# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count=defaultdict(int)
        
        def traverse(Node):  
            if Node:
                count[Node.val]+=1
                traverse(Node.left)
                traverse(Node.right)

        traverse(root)
        res=[]
        maxx=max(count.values())
        for i in count:
            if count[i]==maxx:
                res.append(i)


        return res
