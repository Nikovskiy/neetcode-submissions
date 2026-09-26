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
        left_c = 1
        right_c = 1
        stack.append((root.left, root.right))

        while stack:

            left, right = stack.pop()

            if left is not None:
                left_c += 1
                stack.append((left.left, left.right))
            if right is not None:
                right_c += 1
                stack.append((right.left, right.right))
            
        return max(left_c, right_c)