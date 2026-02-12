class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(n1, n2):
            if not n1 and not n2:
                return True
            elif not n1 or not n2:
                return False
            else:
                left_symmetric = isMirror(n1.left, n2.right)
                right_symmetric = isMirror(n1.right, n2.left)
                value_symmetric = (n1.val == n2.val)
                return left_symmetric and right_symmetric and value_symmetric
        return isMirror(root.left, root.right)