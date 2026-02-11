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
        #3. queue에 root를 추가하고, c_list 초기화.
        q.append(root)
        while q:
            #4. len(queue)에 대해 pop하고 append.
            # for all nodes at the same level of a queue
            len_q = len(q)
            for _ in range(len_q): 
                n = q.popleft()
                c_list.append(n.val)
                if n.left:
                     q.push(n.left)
                if n.right:
                     q.push(n.right)

        #q가 다 비면 current_list를 final_list에 추가.
        final_list.append(c_list)
        return final_list  
                


            
          