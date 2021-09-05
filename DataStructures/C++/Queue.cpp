#include <iostream>
#include <queue>

template <class T>
struct Node{
    T value;
    Node<T> * next;
};

template <class T>
class Queue{
    public:
        Node<T>* head;
        Queue<T>(){
             head = NULL;
             last = NULL;
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
    // Utilizing my personal implementation
    Queue<std::int16_t> list;
    list.append(1);
    list.append(2);
    list.append(3);
    list.print();
    list.pop();
    list.print();
    list.pop();
    list.pop();
    list.pop();
    list.print();
    list.append(5);
    list.print();

    std::cout << std::endl;
    // This can all be replaced with the following code:
    std::queue<int> list2;
    list2.push(1);
    list2.push(2);
    list2.push(3);
    std::cout << list2.front() << std::endl;
    list2.pop();
    list2.pop();
    list2.pop();
    list2.push(5);
    std::cout << list2.front() << std::endl;


    return 0;
}
