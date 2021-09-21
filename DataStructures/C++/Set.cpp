#include <iostream>
#include <set>
#include <iterator>

int main(){
    std::set<std::int64_t> set;
    set.insert(1);
    set.insert(2);
    set.insert(3);
    set.insert(4);
    set.insert(5);


    std::set<std::int64_t>::iterator itr;
    std::cout << "\nThe set is : \n";
    std::cout << "\tELEMENT\n";
    for (itr = set.begin(); itr != set.end(); ++itr) {
        std::cout << '\t' << *itr << '\n';
    }
    std::cout << std::endl;

    return 0;
}