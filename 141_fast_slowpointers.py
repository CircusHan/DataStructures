class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow와 fast 정의
        slow = head
        fast = head
        # fast가 slow와 같아지는 순간이 오면 True, 아니면 False return하기(처음 같아지는 순간은 제외하기)
        first = True
        while fast is not None and fast.next is not None:
            if fast is slow and first != True:
                return True
            else: 
                first = False
                slow = slow.next
                fast = fast.next.next
            