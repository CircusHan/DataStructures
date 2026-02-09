class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 0
        current = head
        while current is not None:
            current = current.next
            size += 1
        index = size // 2
        current = head
        for i in range(index):
            current = current.next
        return current
        