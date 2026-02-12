class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def PathSum(node, targetSum):
            if not node:
                return False
            else:
                remainder = targetSum - node.val
                l_pathsum = PathSum(node.left, remainder)
                r_pathsum = PathSum(node.right, remainder)
                return l_pathsum or r_pathsum or (remainder==0 and not node.left and not node.right)
        return PathSum(root, targetSum)