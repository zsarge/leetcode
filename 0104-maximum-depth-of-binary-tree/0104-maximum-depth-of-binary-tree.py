# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def search(root: TreeNode, depth: int) -> int:
            if root is None:
                return depth
            return max(search(root.left, depth+1), search(root.right, depth+1))
        return search(root, 0)