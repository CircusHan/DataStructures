from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        #기본 변수들 초기화.
        q = deque()
        final_list = []
        #root가 비어있다면 빈 리스트 반환, 있다면 큐에 넣기.
        
        q.append(root)
        

        #queue에 root 추가하고 나서는 loop 돌며..
        while q:
            c_list = []
            len_q = len(q)
            for _ in range(len_q):
                n = q.popleft()
                c_list.append(n.val)
                #n의 왼쪽 오른쪽이 있는지 없는지에 따라 경우를 나눠야 함.
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
        #final list에 넣기
            final_list.append(c_list)
        reverse_list = final_list[::-1]
        return reverse_list