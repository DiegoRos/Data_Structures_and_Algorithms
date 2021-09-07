class Node:
    def __init__(self, val) -> None:
        self.node = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        new_node = Node(val)
        new_node.next = None

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        elif self.head == self.tail:
            self.tail = new_node
            self.head.next = self.tail
        
        else:
            self.tail.next = new_node
            self.tail = new_node

    
    def pop(self):
        if self.head is None:
            return
        self.head = self.head.next

    def __str__(self) -> str:
        result = ""
        temp = self.head
        while(temp != None):
            if temp.next == None:
                result += f"{temp.node}"
            else:
                result += f"{temp.node} ->"
            temp = temp.next
    

        return result


if __name__ == "__main__":
    a = Queue()
    a.append(1)
    print(a)
    a.append(2)
    print(a)
    a.append(3)
    print(a)
    a.append(5)
    print(a)
    a.pop()
    print(a)
    a.append(7)
    print(a)

    from collections import deque
    b = deque()
    b.append(1)
    print(b)
    b.append(2)
    b.append(3)
    b.append(5)
    print(b)
    b.popleft() # This behaviour would signal queue
    print(b)
    b.popleft() # This behaviour would signal queue
    print(b)