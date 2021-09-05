#include <iostream>
#include <stack>

template <class T>
struct Node{
    T value;
    Node<T> * next;
};

template <class T>
class Stack{
    public:
        Node<T>* head;
        Stack<T>(){
             head = NULL;
        }

        void push(T value){
            Node<T>* new_node = new Node<T>;
            new_node->value = value;
            new_node->next = NULL;
            if(head == NULL){
                head = new_node;
                return;
            }
            else{
                new_node->next = head;
                head = new_node;
            }
        }

        T pop(){
            if (head == NULL){
                return NULL;
            }
            T value = head->value;
            Node<T>* del = head;
            head = head->next;
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
    Stack<std::int16_t> list;
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
    
    std::cout << std::endl;
    // This can all be replaced with the following code:
    std::stack<int> list2;
    list2.push(1);
    list2.push(2);
    list2.push(3);
    std::cout << list2.top() << std::endl;
    list2.pop();
    list2.pop();
    list2.pop();
    list2.push(5);
    std::cout << list2.top() << std::endl;
    return 0;
}
