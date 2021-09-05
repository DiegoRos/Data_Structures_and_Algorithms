class Node:
    def __init__(self, val) -> None:
        self.node = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while(temp.next != None):
            temp = temp.next
        
        temp.next = new_node

    
    def pop(self):
        if self.head is None:
            return
        self.head = self.head.next

    def __str__(self) -> str:
        result = ""
        temp = self.head
        while(temp != None):
            result += f"{temp.node} ->"
            temp = temp.next
    

        return result


if __name__ == "__main__":
    a = LinkedList()
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