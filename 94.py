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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def traverse(node):
            if node != None:
                traverse(node.left)
                print(node.val, end=",")
                result.append(node.val)
                traverse(node.right)
                
        traverse(root)
        return result


arr = [1,2,3,4,5,None,8,None,None,6,7,9]
root = array_to_tree(arr)
sol = Solution()
print(sol.inorderTraversal(root))

