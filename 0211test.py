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
        final_list = []
        q = deque()
        c_list = []
        #1. 빈 트리가 있으면 빈 리스트 반환
        if not root:
              return []
        #2.초기화 final_list, queue, current_list, last_level
        final_list = []
        q = deque()
        c_list = []
        #3. queue에 root를 추가하고, c_list 초기화.
        
        q.append(root)
        while q:
            #4. len(queue)에 대해 pop하고 append.
            len_q = len(q)
            for _ in range(len_q):
                # for all nodes at the same level of a queue
                n = q.popleft()
                c_list.append(n.val)
                #n.left와 n.right가 남아있는지도 확인.
                if n.left:
                      q.push(n.left)
                if n.right:
                      q.push(n.right)


        #q가 다 비면 current_list를 final_list에 추가.
        final_list.append(c_list)
        return final_list  