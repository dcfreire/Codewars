#include <iostream>
using namespace std;

template <int x>
struct factorial {
        static unsigned long long int const value = x * factorial<x-1>::value;
};

template <int x> unsigned long long int const factorial<x>::value;

template <>
struct factorial<0> {
        enum {value = 1};
};



int main(){
 cout << factorial<3>::value << endl;

}
