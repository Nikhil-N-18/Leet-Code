# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        height = 0
        q = deque([root])
        while q:
            length = len(q)
            for i in range(length):
                ele = q.popleft()
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            height += 1
        return height
        