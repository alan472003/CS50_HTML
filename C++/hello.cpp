#include <iostream>
#include <vector>

int main() {
    std::vector<int> v;
    v.push_back(5);
    v.push_back(6);
    v.push_back(3);
    v.push_back(2);
    v.push_back(1);
    v.push_back(4);

    for (int i; i < v.size(); i++)
        std::cout << v[i] << std::endl;

    std::cout << "Hello, World!" << std::endl;
    return 0;
}
