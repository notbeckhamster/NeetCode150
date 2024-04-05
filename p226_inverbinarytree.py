from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.swap_lr(root)
        
        
    def swap_lr(self, root):
        if root is None:
            return root
        temp = root.left
        root.left = root.right
        root.right = temp
        self.swap_lr(root.left)
        self.swap_lr(root.right)
        return root