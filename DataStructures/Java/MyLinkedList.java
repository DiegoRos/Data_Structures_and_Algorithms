package Java;
import java.util.LinkedList;
//If they are in the same package java will recognize the object and the next import is not required, if not use the package declaration in
// the project to specify where the object originates from.
// import Java.GenericNode;

public class MyLinkedList<T>{
    public GenericNode<T> head;
    public GenericNode<T> tail;
    public MyLinkedList(){
        head = null;
        tail = null;
    }

    public void push(T val){
        GenericNode<T> new_node = new GenericNode<>(val);
        if (head == null){
            head = new_node;
            tail = head;
        }
        else{
            new_node.next = head;
            head = new_node;
        }

    }

    public void append(T val){
        GenericNode<T> new_node = new GenericNode<>(val);
        if (head == null){
            head = new_node;
            tail = head;
        }
        else if (head == tail){
            tail = new_node;
            head.next = tail;
        }
        else{
            tail.next = new_node;
            tail = new_node;
        }
    }

    public T pop(){
        if(head == null)
            return null;
        
        T temp = head.head;
        if (head == tail){
            head = null;
            tail = null;
        }
        else{
            head = head.next;
        }

        return temp;
    }

    // A toString() method can be overriden to produce a System.out.print or println representation.
    public void print(){
        if(head == null){
            System.out.println("Stack is Empty");
            return;
        }
        GenericNode<T> temp = head;
        while (temp != null){
            if (temp.next == null)
                System.out.print(temp.head);
            else
                System.out.print(temp.head + " -> ");
            temp = temp.next;
        }
        System.out.println();

    }

    public static void main(String[] args) {
        MyLinkedList<Integer> myList = new MyLinkedList<>();

        myList.push(1);
        myList.push(2);
        myList.push(3);
        myList.print();
        myList.pop();
        myList.print();
        myList.pop();
        myList.pop();
        myList.pop();
        myList.print();
        myList.push(5);
        myList.print();

        // Java implementation:
        LinkedList<Integer> javaList = new LinkedList<>();
        javaList.add(1);
        javaList.add(2);
        javaList.add(3);
        javaList.addFirst(5);// Adds at beginning of list
        javaList.add(2, 7); // Adds at a specific index
        System.out.println(javaList);

        javaList.remove(2);// Removes value if found or index
        javaList.removeFirst(); // Removes first
        javaList.removeLast(); // Removes last
        System.out.println(javaList);

        // This can also be written as a vector
    }
}