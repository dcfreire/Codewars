#include <string>
#include <iostream>
#include <stdlib.h>
#include <vector>

class DirReduction
{
public:
static std::vector<std::string> dirReduc(std::vector<std::string> &arr){

        for(int i = 0; i < arr.size(); i++) {
                        if(!arr[i].compare("NORTH") && !arr[i + 1].compare("SOUTH")) {
                                arr.erase(arr.begin() + i);
                                arr.erase(arr.begin() + i);
                                i = 0;
                        }
                        if(!arr[i].compare("EAST") && !arr[i + 1].compare("WEST")) {
                                arr.erase(arr.begin() + i);
                                arr.erase(arr.begin() + i);
                                i = 0;

                        }
                        if(!arr[i + 1].compare("EAST") && !arr[i].compare("WEST")) {
                                arr.erase(arr.begin() + i);
                                arr.erase(arr.begin() + i);
                                i = 0;



                        }
                        if(!arr[i + 1].compare("NORTH") && !arr[i].compare("SOUTH")) {
                                arr.erase(arr.begin() + i);
                                arr.erase(arr.begin() + i);
                                i = 0;


                        }



        }
        return arr;

}
};

int main(){}
