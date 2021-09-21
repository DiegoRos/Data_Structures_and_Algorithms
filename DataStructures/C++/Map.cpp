#include <iostream>
#include <map>
#include <iterator>

int main(){
    std::map<std::string, std::int64_t> map;
    map.insert(std::pair<std::string, std::int64_t>("Hello", 1));
    map.insert(std::pair<std::string, std::int64_t>("My", 2));
    map.insert(std::pair<std::string, std::int64_t>("Name", 3));
    map.insert(std::pair<std::string, std::int64_t>("Is", 4));
    map.insert(std::pair<std::string, std::int64_t>("Diego", 5));


    std::map<std::string, std::int64_t>::iterator itr;
    std::cout << "\nThe map is : \n";
    std::cout << "\tKEY\tELEMENT\n";
    for (itr = map.begin(); itr != map.end(); ++itr) {
        std::cout << '\t' << itr->first << '\t' << itr->second << '\n';
    }
    std::cout << std::endl;

    return 0;
}