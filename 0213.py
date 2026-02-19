class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def PathSum(node, targetSum):
            if not node:
                return False
            else:
                remainder = targetSum - node.val
                l_pathsum = PathSum(node.left, remainder)
                r_pathsum = PathSum(node.right, remainder)
                return l_pathsum or r_pathsum or (not node.left and not node.right and remainder)
        return PathSum(root, targetSum) 
    
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
                return (left_symmetric and right_symmetric and value_symmetric)
        return isMirror(root.left, root.right)
 
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
            return (left_same and right_same and node_same)
        return isSame(p, q)
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            else:
                left_depth = depth(node.left)
                right_depth = depth(node.right)
                return max(left_depth, right_depth)+1
        return depth(root)
    

 
        