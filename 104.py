#Maximum depth of a Binary tree.
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        q = deque()
        if not root:
            return depth
        q.append(root)
        while q:
            len_q = len(q)
            for _ in range(len_q):
                n = q.popleft()
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            depth += 1
        return depth 

