# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        
        def dfs(curr: Optional[TreeNode], curr_str: str):
            if curr == None:
                return
            
            curr_str = chr(ord('a')+curr.val)+curr_str
            if curr.left and curr.right:
                return min(dfs(curr.left, curr_str), dfs(curr.right, curr_str)) # type: ignore
            elif curr.left:
                return dfs(curr.left, curr_str)
            elif curr.right:
                return dfs(curr.right, curr_str)
            return curr_str
        return dfs(root, "") # type: ignore