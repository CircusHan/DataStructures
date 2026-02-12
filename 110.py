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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(node):
            if not node:
                return (True, 0) #node가 없는 경우
            else:
                left_balanced, left_depth = balanced(node.left)
                right_balanced, right_depth = balanced(node.right)
                depth = max(left_depth, right_depth) + 1
                result = abs(left_depth - right_depth) <= 1 and left_balanced and right_balanced
                #print(result, depth)
                return (result, depth)
        result, _ = balanced(root)
        return result

    

arr = [1,2,2,3,3,None,None,4,4]
root = array_to_tree(arr)
sol = Solution()
print(sol.isBalanced(root))