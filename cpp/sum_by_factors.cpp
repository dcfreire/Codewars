#include <string>
#include <vector>
#include <map>
#include <stdlib.h>
#include <stdio.h>
#include <iostream>
std::map<int, int> is_prime;
class SumOfDivided
{
public:
static bool isPrime(int num) {
        int i;
        if(is_prime[num] == 1){
                return true;
              }
        if(is_prime[num] == 2)
                return false;
        if(num == 2 || num == 3) {
                is_prime[num] = 1;
                return true;

        }
        if(num == 1 || num <= 0 || num %2 == 0 || num % 3 == 0) {
                is_prime[num] = 2;
                return false;
        }
        i = 5;
        while(i*i <= num) {
                if(num % i == 0 || num % (i+2) == 0) {
                        is_prime[num] = 2;

                        return false;
                }
                i += 6;


        }
        is_prime[num] = 1;

        return true;
}

static std::string sumOfDivided(std::vector<int> &lst){
        std::string ret;
        std::map<int, int> aux;
        std::map<int, int>::iterator ptr;
        int sum = 0, iaux, pos;
        for(int i = 0; i < lst.size(); i++) {
                iaux = lst[i];
                pos = abs(iaux);
                if(!(pos %2))
                  pos--;
                while(pos > 1) {
                        if(isPrime(pos)) {
                                if(!(iaux % pos)) {
                                        iaux /= pos;
                                        aux[pos] += lst[i];

                                }

                        }if(pos > 3)
                          pos -= 2;
                        else
                          pos --;
                }
        }
        for(ptr = aux.begin(); ptr != aux.end(); ++ptr) {
                ret.append("(");
                ret.append(std::to_string(ptr->first));
                ret.append(" ");
                ret.append(std::to_string(aux[ptr->first]));
                ret.append(")");
        }
        return ret;
}
};

/*int main(){
        std::vector<int> lst = {12, 15};
        std::cout << SumOfDivided::sumOfDivided(lst);
}*/
