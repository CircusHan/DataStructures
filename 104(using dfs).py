class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            else:
                l_depth = depth(node.left)
                r_depth = depth(node.right)
            return 1 + max(l_depth, r_depth)
        return depth(root)
        