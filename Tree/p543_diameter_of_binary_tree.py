# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(curr):
            if curr == None:
                return 0
            left_height = dfs(curr.left)
            right_height = dfs(curr.right)
            self.res = max(self.res, left_height+right_height)
            return 1+max(left_height, right_height)
        dfs(root)
        return self.res