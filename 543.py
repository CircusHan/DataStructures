#Diameter of Binary Tree.
from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def array_to_tree(arr):
    if not arr: return None
    
    root = TreeNode(arr[0])
    queue = deque([root]) 
    i = 1
    
    # Iterate while there are nodes in queue
    while queue and i < len(arr):
        node = queue.popleft()
        
        # Link Left Child
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        
        # Link Right Child
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
        
    return root



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def diameter(node):
            if not node:
                return (0, 0)
            #양쪽의 새 path와 더해서 더 값이 크거나, 기존 왼/오른쪽의 diameter값이 더 크거나.
            left_h, left_diameter = diameter(node.left)
            right_h, right_diameter = diameter(node.right)
            height = max(left_h, right_h)+1
            c_diameter = left_h + right_h #node를 반드시 포함하는 diameter.
            dia = max(c_diameter, left_diameter, right_diameter) #기존 두개의 diameter랑 비교해서 최대.

            return (height, dia)
        
        _, dia = diameter(root)
        return dia
    

arr = [1,2,3,4,5]
root = array_to_tree(arr)
sol = Solution()
print(sol.diameterOfBinaryTree(root))