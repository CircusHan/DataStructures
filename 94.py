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

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #final_list 라는 최종 아웃풋 필요
        #deque가 필요함
        #c_list가 필요함

        #1. 빈 트리가 있으면 빈 리스트 반환
        if not root:
            return []
        #2.초기화 final_list, queue, current_list, last_level
        final_list = []
        q = deque()
        c_list = []
        last_level = 0

        q.append(root)
        while q:
            c_list = []
            for _ in range(len(q)): # for all nodes at the same level of a queue
                n = q.popleft()
                c_list.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            
            final_list.append(c_list)
        return final_list
        
        '''
        #3. queue의 (root,0)을 push
        q.append((root, 0))
        #4. while queue is not empty
        while q:
            #5. (node, level) = queue.pop()
            (n, level) = q.popleft()
            #6. 레벨이 바뀌었으면 이전의 current list를 final_list에 append하기. current_list 초기화하기
            if level > last_level:
                last_level += 1
                final_list.append(c_list)
                c_list = []
            #7. current_list에다 node.val을 append하기.
            c_list.append(n.val)
            #8. current의 자식 노드에 대해서 자식을 queue에 넣기 + 레벨 증가.
            if n.left:
                q.append((n.left, level+1))
            if n.right:
                q.append((n.right, level+1))
            
        #final_list에 남아있는 current_list 넣기
        final_list.append(c_list)
        # print(final_list)
        return final_list
        '''
        
        

arr = [1,2,3,4,5]
root = array_to_tree(arr)
sol = Solution()
# print(sol.inorderTraversal(root))
# print(sol.preorderTraversal(root))
# print(sol.postorderTraversal(root))
print(sol.levelOrder(root))
