class Node:
    def __init__(self, val=0,  next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def print(self):
        curr = self.head
        print('[', end="")
        while curr is not None:
            print(f'{curr.val}', end=",")
            curr = curr.next
        print(']')


    def reverse(self)->Node:
        #초기 prev, curr, succ 설정
        prev = None
        curr = self.head
        while curr is not None: # prev, curr, succ의 위치 옮겨가면서 curr.next prev 가리키게끔 하기
            succ = curr.next
            curr.next = prev
            prev = curr # curr.next 의 화살표를 prev로 옮기면서 succ와의 연결이 끊어지므로 curr = succ, succ = curr.next로 저장하며 이동해야 함.
            curr = succ
        self.head = prev

    

    def append(self, val):
        n = Node(val)
        if self.head is None: # head 뒤에 아무것도 없는 경우
            self.head = n
            return 
        else:  # head 뒤에 노드들이 있는 경우
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = n

lst = SinglyLinkedList()
lst.append(3)
lst.append(4)
lst.append(5)
lst.print()
lst.reverse()
lst.print()