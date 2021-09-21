package Java;
//If they are in the same package java will recognize the object and the next import is not required, if not use the package declaration in
// the project to specify where the object originates from.
// import Java.GenericNode;

import java.util.LinkedList;
import java.util.Queue;

public class MyQueue<T>{
    public GenericNode<T> head;
    public GenericNode<T> tail;
    public MyQueue(){
        head = null;
        tail = null;
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
        MyQueue<Integer> myList = new MyQueue<>();

        myList.append(1);
        myList.append(2);
        myList.append(3);
        myList.print();
        myList.pop();
        myList.print();
        myList.pop();
        myList.pop();
        myList.pop();
        myList.print();
        myList.append(5);
        myList.print();

        // Java implementation:
        Queue<Integer> javaList = new LinkedList<>(); // Queue is an interface, therefore we cannot create an object of type Queue.
        javaList.add(1);
        javaList.add(2);
        javaList.add(3);
        javaList.add(4);
        javaList.add(5);
        System.out.println(javaList);

        javaList.remove();// Removes value if found or index
        javaList.remove(); 
        javaList.remove();
        System.out.println(javaList);
    }
}