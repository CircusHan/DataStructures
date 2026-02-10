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
        #loop: 각 curr 노드마다 prev succ 설정해야 하고
        curr = self.head
        prev = None
        
        while curr is not None:
            #curr.next가 prev를 포인트하도록 변경
            succ = curr.next
            curr.next = prev
            prev = curr
            curr = succ
        self.head = prev
        return prev

    

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