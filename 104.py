#Maximum depth of a Binary tree.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        final_list = []
        q = deque()
        c_list = []
        level = 0
        if not root:
            return depth
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
            final_list.append(c_list)
            depth += 1
        return depth 

