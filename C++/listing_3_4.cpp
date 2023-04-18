#include <iostream>

int main()
{
    using std::cout;
    using std::endl;

    unsigned short int smallNumber;
    smallNumber = 65535;

    cout << "smallNumber: " << smallNumber << endl;
    smallNumber++;
    cout << "smallNumber: " << smallNumber << endl;
    smallNumber++;
    cout << "smallNumber: " << smallNumber << endl;

    return 0;
}