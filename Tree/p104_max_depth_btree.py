# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        l_max = self.maxDepth(root.left)+1
        r_max = self.maxDepth(root.right)+1
        return max(l_max, r_max)