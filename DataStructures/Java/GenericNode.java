package Java;

public class GenericNode<T> {
    public T head;
    public GenericNode<T> next;
    public GenericNode(T element){
        head = element;
        next = null;
    }
}
