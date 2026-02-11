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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final_list = []
        q = deque()
        c_list = []
        level = 0
        if not root:
            return []
        q.append(root)
        while q:
            len_q = len(q)
            for _ in range(len_q):
                n = q.popleft()
                c_list.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            if level % 2 == 0:
                final_list.append(c_list)
            else:
                rev_list = c_list[::-1]
                final_list.append(rev_list)
            c_list = []
            level += 1
                
                
        return final_list

arr = [3,9,20,None,None,15,7]
root = array_to_tree(arr)
sol = Solution()
print(sol.zigzagLevelOrder(root))

