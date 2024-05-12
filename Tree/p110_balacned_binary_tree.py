# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def dfs(curr):
            if curr == None:
                return 0
            
            left_height = dfs(curr.left)
            right_height = dfs(curr.right)
            diff = abs(left_height - right_height)
            if diff > 1:
                self.is_balanced=False
            return 1+max(left_height, right_height)
        dfs(root)
        return self.is_balanced
        