class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSame(n1, n2):
            if not n1 and not n2:
                return True
            elif not n1 or not n2:
                return False
            else:
                left_same = isSame(n1.left, n2.left)
                right_same = isSame(n1.right, n2.right)
                node_same = (n1.val == n2.val)
                return left_same and right_same and node_same
        return isSame(p, q)