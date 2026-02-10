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
        def inorder(node):
            if node != None:
                inorder(node.left)
                print(node.val, end=",")
                result.append(node.val)
                inorder(node.right)
                
        inorder(root)
        return result
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(node):
            if node != None:
                print(node.val, end=",")
                result.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return result
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def postorder(node):
            if node != None:
                postorder(node.left)
                postorder(node.right)
                print(node.val, end=",")
                result.append(node.val)

        postorder(root)
        return result


arr = [1,2,3,4,5]
root = array_to_tree(arr)
sol = Solution()
print(sol.inorderTraversal(root))
print(sol.preorderTraversal(root))
print(sol.postorderTraversal(root))

