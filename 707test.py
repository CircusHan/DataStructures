class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
       self.head = Node(None)
       self.tail = Node(None)
       self.head.next = self.tail
       self.tail.prev = self.head
       self.size = 0
    
    def print(self):
        current = self.head
        print('[', end="")
        for i in range(self.size):
            current = current.next
            print(f'{current.val}', end="")
        print(']')
        
    def isEmpty(self):
        return self.head.next is self.tail

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        else:
            current = self.head
            for i in range(index+1):
                current = current.next
            return current.val
        
    def add(self, prev, curr, succ) -> None:
        curr.prev = prev
        curr.next = succ
        prev.next = curr
        succ.prev = curr
        

    def addAtHead(self, val: int) -> None:
        self.size += 1
        n = Node(val)
        self.add(self.head, n, self.head.next)
        self.print()

    def addAtTail(self, val: int) -> None:
        self.size += 1
        n = Node(val)
        self.add(self.tail.prev, n, self.tail)
        self.print()

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return None
        self.size += 1
        n = Node(val)
        current = self.head
        for i in range(index+1):
            current = current.next
        self.add(current.prev, n, current)
        self.print()

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None
        self.size -= 1
        current = self.head
        for i in range(index+1):
            current = current.next
        prev = current.prev
        succ = current.next
        prev.next = succ
        succ.prev = prev

def run_test_case(commands, inputs):
    """
    commands: 실행할 함수 이름 리스트 (예: ["MyLinkedList", "addAtHead", ...])
    inputs: 각 함수에 전달할 인자 리스트 (예: [[], [1], ...])
    """
    obj = None
    results = []

    for cmd, params in zip(commands, inputs):
        if cmd == "MyLinkedList":
            obj = MyLinkedList()
            results.append(None) # 생성자는 반환값이 없음 (null)
        
        elif cmd == "addAtHead":
            obj.addAtHead(params[0])
            results.append(None)
            
        elif cmd == "addAtTail":
            obj.addAtTail(params[0])
            results.append(None)
            
        elif cmd == "addAtIndex":
            # params 예: [1, 2] -> index=1, val=2
            obj.addAtIndex(params[0], params[1])
            results.append(None)
            
        elif cmd == "get":
            val = obj.get(params[0])
            results.append(val)
            
        elif cmd == "deleteAtIndex":
            obj.deleteAtIndex(params[0])
            results.append(None)
            
    return results

# --- 실행 및 검증 ---

# 예제 입력 데이터
commands = ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
params = [[],[1],[3],[1,2],[1],[1],[1]]

# 드라이브 실행
output = run_test_case(commands, params)

# 결과 출력 (Python의 None을 문제의 null 표현에 맞게 변환하여 출력)
formatted_output = ["null" if x is None else x for x in output]
print("Input Commands:", commands)
print("Input Params:  ", params)
print("-" * 30)
print("Actual Output:  ", formatted_output)
print("Expected Output: ['null','null','null','null','null','null','null','null',4,'null','null','null']")