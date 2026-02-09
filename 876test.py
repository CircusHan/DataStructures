class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # linked list의 사이즈를 구한다.
        size = 0
        current = head
        while current is not None:
            current = current.next
            size += 1
        #middle index = size // 2
        index = size // 2
        # 중앙 노드를 return하기
        current = head
        for i in range(index):
            current = current.next
        return current