# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def depth(node: TreeNode) -> int:
            nonlocal max_diameter
            if node is None:
                return 0
            left_distance = depth(node.left)
            right_distance = depth(node.right)
            max_diameter = max(max_diameter, left_distance+right_distance)
            return 1+max(left_distance, right_distance)
        depth(root)
        return max_diameter