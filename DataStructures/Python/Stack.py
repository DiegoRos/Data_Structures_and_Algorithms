class Node:
    def __init__(self, val) -> None:
        self.node = val
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    
    def pop(self):
        if self.head is None:
            return
        val = self.head.node
        self.head = self.head.next
        return val


    def __str__(self) -> str:
        result = ""
        temp = self.head
        while(temp != None):
            result += f"{temp.node} ->"
            temp = temp.next
    

        return result


if __name__ == "__main__":
    a = Stack()
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