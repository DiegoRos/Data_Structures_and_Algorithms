package Java;
//If they are in the same package java will recognize the object and the next import is not required, if not use the package declaration in
// the project to specify where the object originates from.
// import Java.GenericNode;

import java.util.Stack;

public class MyStack<T>{
    public GenericNode<T> head;
    public GenericNode<T> tail;
    public MyStack(){
        head = null;
    }

    public void push(T val){
        GenericNode<T> new_node = new GenericNode<>(val);
        if (head == null){
            head = new_node;
        }
        else{
            new_node.next = head;
            head = new_node;
        }

    }


    public T pop(){
        if(head == null)
            return null;
        
        T temp = head.head;
        head = head.next;
        return temp;
    }

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
        MyStack<Integer> myList = new MyStack<>();

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
        Stack<Integer> javaList = new Stack<>();
        javaList.push(1);
        javaList.push(2);
        javaList.push(3);
        javaList.push(4);
        javaList.push(5);
        System.out.println(javaList);

        javaList.pop();// Removes value if found or index
        javaList.pop(); // Removes first
        javaList.pop(); // Removes last
        System.out.println(javaList);
    }
}