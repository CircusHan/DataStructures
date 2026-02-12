class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            else:
                left_depth = depth(node.left)
                right_depth = depth(node.right)
                if not node.left or not node.right:
                    return 1 + max(left_depth, right_depth)
                else:
                    return 1 + min(left_depth, right_depth)
        return depth(root)