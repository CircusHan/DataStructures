class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        while current is not None and not hasattr(current, 'visited'):
            current.visited = True
            current = current.next
        if current is None:
            return False
        else:
            return True