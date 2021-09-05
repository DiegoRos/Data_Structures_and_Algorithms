#include <iostream>

template <class T>
struct Node{
    T value;
    Node<T> * next;
};

template <class T>
class LinkedList{
    public:
        Node<T>* head;
        LinkedList<T>(){
             head = NULL;
             last = NULL;
        }

        void push(T value){
            Node<T>* new_node = new Node<T>;
            new_node->value = value;
            new_node->next = NULL;
            if(head == NULL){
                head = new_node;
                last = new_node;
                return;
            }
            else{
                new_node->next = head;
                head = new_node;
            }
        }

        void append(T value){
            Node<T>* new_node = new Node<T>;
            new_node->value = value;
            new_node->next = NULL;
            if(head == NULL){
                head = new_node;
                last = new_node;
                return;
            }
            else if (last == head){
                last = new_node;
                head->next = last;
            }
            else{
                last->next = new_node;
                last = new_node;
            }
        }

        T pop(){
            if (head == NULL){
                return NULL;
            }
            T value = head->value;
            Node<T>* del = head;
            if (head == last){
                head = NULL;
                last = NULL;
            }
            else{
                head = head->next;
            }
            delete del;
            return value;
        }

        void print(){
            if(head == NULL){
                std::cout << "Stack is Empty" << std::endl;
                return;
            }
            Node<T>* temp = head;
            while (temp){
                if (temp->next == NULL)
                    std::cout << temp->value;
                else
                    std::cout << temp->value << " -> ";
                temp = temp->next;
            }
            std::cout << std::endl;

        }
    private:
        Node<T>* last;

};

int main(){
    LinkedList<std::int16_t> list;
    list.push(1);
    list.push(2);
    list.push(3);
    list.print();
    list.pop();
    list.print();
    list.pop();
    list.pop();
    list.pop();
    list.print();
    list.push(5);
    list.print();

    // This can be replicated in C++ 11 with:
    // #include <forward_list>
    // forward_list <int> myList;

    return 0;
}
