# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = []
        depth = 1
        max_depth = 0
        stack.append((root.left, depth))
        stack.append((root.right, depth))
        while stack:

            node, depth = stack.pop()

            if node:
                depth += 1
                stack.append((node.left, depth))
                stack.append((node.right, depth))
            max_depth = max(depth, max_depth)

            
        return max_depth