#Diameter of Binary Tree.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def diameter(node):
            if not node:
                return 0
            
            left_h = diameter(node.left)
            right_h = diameter(node.right)

            length = left_h + right_h
            self.max_diameter = max(self.max_diameter, length)

            return 1 + max(left_h, right_h)
        
        diameter(root)
        return self.max_diameter
            